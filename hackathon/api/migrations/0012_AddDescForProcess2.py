# Generated by Django 2.1.7 on 2019-12-01 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackathon', '0011_AddDescForBaseProcess'),
    ]

    operations = [
        migrations.AddField(
            model_name='process',
            name='description',
            field=models.TextField(default='', null=True, verbose_name='Описание процесса'),
        ),
    ]