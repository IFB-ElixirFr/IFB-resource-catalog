# Generated by Django 2.2 on 2020-01-21 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0023_auto_20200121_1515'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tool',
            name='language',
        ),
    ]
