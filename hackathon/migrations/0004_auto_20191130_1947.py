# Generated by Django 2.1.7 on 2019-11-30 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackathon', '0003_auto_20191130_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='creation_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата создания'),
        ),
    ]
