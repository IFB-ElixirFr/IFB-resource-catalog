# Generated by Django 2.2 on 2020-01-21 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0030_auto_20200121_1600'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uri', models.CharField(blank=True, max_length=100, null=True)),
                ('term', models.CharField(blank=True, max_length=100, null=True)),
                ('additionDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='tool',
            name='topic',
        ),
        migrations.AddField(
            model_name='tool',
            name='topic',
            field=models.ManyToManyField(blank=True, to='database.Topic'),
        ),
    ]