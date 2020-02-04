from django.core.management import BaseCommand
from django.core.management import call_command

from database.models import Tool
from database.models import ToolType
from database.models import Language
from database.models import Topic
from database.models import OperatingSystem
from database.models import Publication
from database.models import Link
from database.models import Download
from database.models import Relation
from database.models import Collection
from database.models import OtherID
from database.models import Version
from database.models import ElixirPlatform
from database.models import ElixirNode
from database.models import Accessibility
from database.models import ToolCredit


from catalogue.settings import BASE_DIR
import urllib3
import json

class Command(BaseCommand):
    def crawl_tools(self, limit):
        """
        transforms a biotool entry in RDF using common vocabularies.
        :param connection: credentials, possibly proxy, and URL to connect to
        :param limit: an integer value specifying the number of entries to transform, -1 means no limit.
        :return: a string representation of the corresponding JSON-LD document
        """
        Tool.objects.all().delete()
        ToolType.objects.all().delete()
        Language.objects.all().delete()
        Topic.objects.all().delete()
        OperatingSystem.objects.all().delete()
        Publication.objects.all().delete()
        Link.objects.all().delete()
        Download.objects.all().delete()
        Relation.objects.all().delete()
        Collection.objects.all().delete()
        OtherID.objects.all().delete()
        Version.objects.all().delete()
        ElixirPlatform.objects.all().delete()
        ElixirNode.objects.all().delete()
        Accessibility.objects.all().delete()
        ToolCredit.objects.all().delete()


        http = urllib3.PoolManager()
        try:
            req = http.request('GET', 'https://bio.tools/api/tool/?page=1&format=json')
            countJson = json.loads(req.data.decode('utf-8'))
            count = int(countJson['count'])
            print(str(count)+ " available BioTools entries")

            i = 1
            nbTools = 1
            hasNextPage = True
            while hasNextPage :
                req = http.request('GET', 'https://bio.tools/api/tool/?page=' + str(i) + '&format=json')
                try:
                    entry = json.loads(req.data.decode('utf-8'))
                except JSONDecodeError as e:
                    print("Json decode error for " + str(req.data.decode('utf-8')))
                    break

                hasNextPage = (entry['next'] != None)
                # print("Processing page "+str(i)+ " hasNext="+str(hasNextPage
                for tool in entry['list']:
                    # if 'FR' in tool['collectionID']:
                    # if 'elixir-fr-sdp-2019' in tool['collectionID']:

                        # print(tool['name'])
                        # print(tool['link'])
                        # print(tool['credit'])
                        # print(tool[''])

                        # insert in DB tool table here
                        tool_entry, created = Tool.objects.get_or_create(
                            name  = tool['name'],
                            # description = tool['description'],
                            # operating_system = tool['operatingSystem'],
                            # topic = tool['topic'],
                            # link = tool['link'],
                            biotoolsID = tool['biotoolsID'],
                            biotoolsCURIE = tool['biotoolsCURIE'],
                            # software_version = tool['version'],
                            # downloads = tool['download'],
                            tool_license = tool['license'],
                            # language = tool['language'],
                            # otherID = tool['otherID'],
                            maturity = tool['maturity'],
                            homepage = tool['homepage'],
                            # collectionID = tool['collectionID'],
                            credit = tool['credit'],
                            # elixirPlatform = tool['elixirPlatform'],
                            # elixirNode = tool['elixirNode'],
                            cost = tool['cost'],
                            # accessibility = tool['accessibility'],
                            function = tool['function'],
                            # relation = tool['relation'],

                        )
                        tool_entry.save()

                        # insert or get DB tooltype table here
                        self.add_many_to_many_entry_array(tool_entry, tool_entry.tool_type, tool['toolType'], ToolType)
                        # for tooltype in tool['toolType']:
                        #     tool_type_entry, created = ToolType.objects.get_or_create(
                        #         name=tooltype
                        #     )
                        #     tool_type_entry.save()
                        #     tool_entry.tool_type.add(tool_type_entry.id)

                        # insert or get DB language_entry table here
                        self.add_many_to_many_entry_array(tool_entry, tool_entry.language, tool['language'], Language)

                        # insert collectionID entry
                        self.add_many_to_many_entry_array(tool_entry, tool_entry.collection, tool['collectionID'], Collection)

                        # insert ElixirPlatform entry
                        self.add_many_to_many_entry_array(tool_entry, tool_entry.elixir_platform, tool['elixirPlatform'], ElixirPlatform)

                        # insert ElixirNode entry
                        self.add_many_to_many_entry_array(tool_entry, tool_entry.elixir_node, tool['elixirNode'], ElixirNode)

                        # insert accessibility entry
                        self.add_many_to_many_entry_array(tool_entry, tool_entry.accessibility, tool['accessibility'], Accessibility)

                        # insert accessibility entry
                        self.add_many_to_many_entry_array(tool_entry, tool_entry.operatingSystem, tool['operatingSystem'], OperatingSystem)


                        # insert or get DB topic entry table here
                        for topic in tool['topic']:
                            topic_entry, created = Topic.objects.get_or_create(
                                term = topic['term'],
                                uri = topic['uri']
                            )
                            topic_entry.save()
                            tool_entry.topic.add(topic_entry.id)

                        # # insert os entry
                        # for os in tool['operatingSystem']:
                        #     OperatingSystem.objects.create(
                        #         name = os,
                        #         tool = tool_entry
                        #     )

                        # entry for publications
                        for publication in tool['publication']:
                            publication_entry, created = Publication.objects.get_or_create(
                                doi = publication['doi'],
                                pmid = publication['pmid'],
                                pmcid = publication['pmcid'],
                                note = publication['note'],
                                version = publication['version'],
                                type = publication['type'],
                            )
                            publication_entry.save()
                            tool_entry.publication.add(publication_entry.id)

                        # entry for toolCredit
                        for credit in tool['credit']:
                            toolCredit_entry, created = ToolCredit.objects.get_or_create(
                                name = credit['name'],
                                email = credit['email'],
                                url = credit['url'],
                                orcidid = credit['orcidid'],
                                gridid = credit['gridid'],
                                typeEntity = credit['typeEntity'],
                                typeRole = credit['typeRole'],
                                note = credit['note']
                            )
                            toolCredit_entry.save()
                            tool_entry.toolCredit.add(toolCredit_entry.id)

                        # entry for link
                        for link in tool['link']:
                            Link.objects.create(
                                url = link['url'],
                                type = link['type'],
                                note = link['note'],
                                tool = tool_entry
                            )

                        # entry for download
                        for download in tool['download']:
                            Download.objects.create(
                                url = download['url'],
                                type = download['type'],
                                version = download['version'],
                                note = download['note'],
                                tool = tool_entry
                            )

                        # entry for relation
                        for relation in tool['relation']:
                            Relation.objects.create(
                                biotoolsID = relation['biotoolsID'],
                                type = relation['type'],
                                tool = tool_entry
                            )

                        # entry for otherID
                        for otherID in tool['otherID']:
                            OtherID.objects.create(
                                value = otherID['value'],
                                type = otherID['type'],
                                version = otherID['version'],
                                tool = tool_entry
                            )

                        # entry for version
                        for version in tool['version']:
                            Version.objects.create(
                                version = version,
                                tool = tool_entry
                            )




                        nbTools += 1
                        progress = nbTools * 100 / count
                        if (nbTools % 500 == 0) :
                            print(str(round(progress))+" % done")
                        if ((limit != -1) and (nbTools >= limit+1)):
                            return
                i+=1
        except urllib3.exceptions.HTTPError as e:
            print("Connection error")
            print(e)
            return None

    def add_many_to_many_entry_array(self, tool_entry, tool_to_field, tool_field, field_class):
        for field_value in tool_field:
            field_entry, created = field_class.objects.get_or_create(
                name = field_value
            )
            field_entry.save()
            tool_to_field.add(field_entry.id)


    def add_arguments(self, parser):
        """
        Arguments for the command line load_biotools
        """
        parser.add_argument(
            '-l',
            '--limit',
            help='Number of tools to import (-1 to retrieve all)',
            type=int,
            default=-1
        )

    def handle(self, *args, **options):
        """
        Call the function to import data
        """
        self.crawl_tools(options['limit'])
