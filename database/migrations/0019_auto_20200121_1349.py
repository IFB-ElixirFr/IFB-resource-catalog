# Generated by Django 2.2 on 2020-01-21 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0018_tool_function'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tool',
            name='function',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
    ]
