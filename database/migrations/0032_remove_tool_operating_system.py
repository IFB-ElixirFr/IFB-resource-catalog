# Generated by Django 2.2 on 2020-01-21 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0031_auto_20200121_1611'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tool',
            name='operating_system',
        ),
    ]
