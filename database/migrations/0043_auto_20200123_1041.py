# Generated by Django 2.2 on 2020-01-23 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0042_auto_20200123_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tool',
            name='credit',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tool',
            name='function',
            field=models.TextField(blank=True, null=True),
        ),
    ]
