# Generated by Django 3.0.3 on 2020-02-12 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0057_auto_20200212_1043'),
    ]

    operations = [
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uri', models.TextField(blank=True, null=True)),
                ('term', models.TextField(blank=True, null=True)),
                ('additionDate', models.DateTimeField(auto_now_add=True)),
                ('function', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='operation', to='database.Function')),
            ],
        ),
    ]
