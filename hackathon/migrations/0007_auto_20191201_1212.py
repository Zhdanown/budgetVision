# Generated by Django 2.1.7 on 2019-12-01 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hackathon', '0006_auto_20191201_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institute',
            name='founder',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hackathon.Institute', verbose_name='Учредитель'),
        ),
        migrations.AlterField(
            model_name='institute',
            name='institute_type',
            field=models.CharField(choices=[('BUDJET_INSTITUTE', 'Бюджетная организация'), ('AUTONOMOUS_INSTITUTE', 'Автономная организация'), ('PUBLIC_INSTITUTE', 'Казенное учреждение'), ('GOVERNMENT_INSTITUTE', 'Государственное унитарное предприятие')], max_length=255),
        ),
        migrations.DeleteModel(
            name='Founder',
        ),
    ]