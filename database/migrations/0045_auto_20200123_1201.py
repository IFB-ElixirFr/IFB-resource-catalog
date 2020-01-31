# Generated by Django 2.2 on 2020-01-23 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0044_auto_20200123_1142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tool',
            name='otherID',
        ),
        migrations.CreateModel(
            name='OtherID',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=1000)),
                ('type', models.TextField(blank=True, null=True)),
                ('version', models.TextField(blank=True, null=True)),
                ('additionDate', models.DateTimeField(auto_now_add=True, null=True)),
                ('tool', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='otherID', to='database.Tool')),
            ],
        ),
    ]
