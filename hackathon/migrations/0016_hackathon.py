# Generated by Django 2.1.7 on 2019-12-01 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackathon', '0015_AddToInstanseForDocument'),
    ]

    operations = [
        migrations.AddField(
            model_name='process',
            name='status',
            field=models.CharField(blank=True, choices=[('DONE', 'Сделано'), ('OVERDUE', 'Просрочены'), ('IN_PROCESS', 'Нужно сделать')], max_length=255, null=True),
        ),
    ]