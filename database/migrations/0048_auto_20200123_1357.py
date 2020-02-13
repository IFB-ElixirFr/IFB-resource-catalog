# Generated by Django 2.2 on 2020-01-23 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0047_auto_20200123_1355'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='elixirnode',
            name='elixirNode',
        ),
        migrations.RemoveField(
            model_name='elixirplatform',
            name='elixirPlatform',
        ),
        migrations.AddField(
            model_name='elixirnode',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='elixirplatform',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]