# Generated by Django 2.2 on 2020-01-23 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0049_auto_20200123_1626'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='operatingsystem',
            name='tool',
        ),
        migrations.AddField(
            model_name='tool',
            name='operatingSystem',
            field=models.ManyToManyField(blank=True, to='database.OperatingSystem'),
        ),
    ]
