# Generated by Django 2.1.7 on 2019-12-01 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackathon', '0012_AddDescForProcess2'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinstitutes',
            name='description',
            field=models.TextField(blank=True, default='', null=True, verbose_name='Описание процесса'),
        ),
        migrations.AlterField(
            model_name='baseprocess',
            name='description',
            field=models.TextField(blank=True, default='', null=True, verbose_name='Описание процесса'),
        ),
        migrations.AlterField(
            model_name='process',
            name='description',
            field=models.TextField(blank=True, default='', null=True, verbose_name='Описание процесса'),
        ),
    ]
