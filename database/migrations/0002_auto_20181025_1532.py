# Generated by Django 2.1.2 on 2018-10-25 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='credit',
            name='adress',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='communities',
            field=models.TextField(),
        ),
    ]