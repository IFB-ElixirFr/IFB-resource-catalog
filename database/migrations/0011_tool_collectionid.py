# Generated by Django 2.2 on 2020-01-21 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0010_tool_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='tool',
            name='collectionID',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
