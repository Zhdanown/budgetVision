"""
Definition of models.
"""

from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class Meta:
        db_table = 'users'
        verbose_name = u'Пользователь'
        verbose_name_plural = u'Пользователи'
    
    TIN = models.CharField('ИНН', max_length=12, null=True, blank=True)
    institutes = models.ManyToManyField('Institute', related_name='user_institutes', verbose_name='Доступные организации')

class HackathonBase(models.Model):
    class Meta:
        abstract = True

    creation_time = models.DateTimeField('Дата создания')

class HackathonDictionary(HackathonBase):
    class Meta:
        abstract = True

    name = models.CharField('Наименование')



class Document(HackathonBase):
    class Meta:
        db_table = 'documents'
        verbose_name = 'Документы'
        verbose_name_plural = 'Документы'

    type = models.ForeignKey('','Тип документа')
    number = models.CharField('Номер', max_length=255)
    creation_date = models.DateTimeField('Дата создания')
    approval_date = models.DateTimeField('Дата утверждения')
    institute = models.ForeignKey('Institute',on_delete=models.PROTECT, verbose_name='Организация')


class Institute(HackathonDictionary):
    class Meta:
        db_table = 'institute'
        verbose_name = 'Учреждение'
        verbose_name_plural = 'Учреждение'

    INSTITUTE_TYPE_CHOICES = []
    TIN = models.CharField('ИНН учреждения', max_length=12, blank=True)
    founder = models.ForeignKey('Founder', on_delete=models.SET_NULL, verbose_name = 'Учредитель', null=True, blank=True)
    institute_type = models.CharField(max_length=255, choices = INSTITUTE_TYPE_CHOICES)


class Founder(HackathonDictionary):
    class Meta:
        db_table = 'founder'
        verbose_name = 'Учредитель'
        verbose_name_plural = 'Учредитель'
    
    TIN = models.CharField('ИНН', max_length=12, blank=True)


class BaseProcess(HackathonDictionary):
    class Meta:
        db_table = 'base_process'
        verbose_name = 'Шаблон процесса'
        verbose_name_plural = 'Шаблон процесса'

    parent_process = models.ForeignKey('BaseProcess', verbose_name='Родитель', null=True)


class Process(HackathonBase):
    class Meta:
        db_table = 'process'
        verbose_name = 'Процесс'
        verbose_name_plural = 'Процесс'

    process = models.ForeignKey('BaseProcess', null=False, on_delete=models.PROTECT)
    from_institute = models.ForeignKey(Institute, verbose_name='Отправитель')
    to_institute = models.ForeignKey(Institute, verbose_name='Получатель')
    document_type = models.ForeignKey('document_types')
    expiration_date = models.DateField()
    



class DocumentTypes(HackathonDictionary):
    class Meta:
        db_table = 'document_types'
        verbose_name = 'Типы документов'
        verbose_name_plural = 'Типы документов'









