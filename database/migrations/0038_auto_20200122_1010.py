# Generated by Django 2.2 on 2020-01-22 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0037_link'),
    ]

    operations = [
        migrations.RenameField(
            model_name='link',
            old_name='tool_id',
            new_name='tool',
        ),
        migrations.RenameField(
            model_name='operatingsystem',
            old_name='tool_id',
            new_name='tool',
        ),
    ]
