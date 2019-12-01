from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


class HackathonBase(models.Model):
    class Meta:
        abstract = True

    creation_time = models.DateTimeField('Дата создания', auto_now_add=True)

class HackathonDictionary(HackathonBase):
    class Meta:
        abstract = True

    name = models.CharField('Наименование', max_length=255)


class DocumentTypes(HackathonDictionary):
    class Meta:
        db_table = 'document_types'
        verbose_name = 'Типы документов'
        verbose_name_plural = 'Типы документов'

    def __str__(self):
        return self.name


class Document(HackathonBase):
    class Meta:
        db_table = 'documents'
        verbose_name = 'Документы'
        verbose_name_plural = 'Документы'

    type = models.ForeignKey(DocumentTypes, verbose_name = 'Тип документа', on_delete=models.PROTECT)
    number = models.CharField('Номер', max_length=255)
    creation_date = models.DateTimeField('Дата создания', null=True, blank=True)
    approval_date = models.DateTimeField('Дата утверждения', null=True, blank=True)
    institute = models.ForeignKey('Institute', on_delete=models.PROTECT, verbose_name='Организация')

    def __str__(self):
        return '%s (%s)' % (self.type.name, self.number)


class Institute(HackathonDictionary):
    class Meta:
        db_table = 'institute'
        verbose_name = 'Учреждение'
        verbose_name_plural = 'Учреждение'

    INSTITUTE_TYPE_CHOICES = [('BUDJET_INSTITUTE', 'Бюджетная организация'),
                             ('AUTONOMOUS_INSTITUTE', 'Автономная организация'),
                             ('PUBLIC_INSTITUTE', 'Казенное учреждение'),
                             ('GOVERNMENT_INSTITUTE', 'Государственное унитарное предприятие'),
                             ]

    TIN = models.CharField('ИНН учреждения', max_length=12, blank=True)
    founder = models.ForeignKey('Institute', on_delete=models.SET_NULL, verbose_name = 'Учредитель', null=True, blank=True)
    institute_type = models.CharField(max_length=255, choices = INSTITUTE_TYPE_CHOICES)

    def __str__(self):
        return self.name


class BaseProcess(HackathonDictionary):
    class Meta:
        db_table = 'base_process'
        verbose_name = 'Шаблон процесса'
        verbose_name_plural = 'Шаблон процесса'
        verbose_name_plural = 'Шаблон процесса'

    parent_process = models.ForeignKey('BaseProcess', verbose_name='Родитель', blank=True, null=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Process(HackathonBase):
    class Meta:
        db_table = 'process'
        verbose_name = 'Процесс'
        verbose_name_plural = 'Процесс'

    process = models.ForeignKey('BaseProcess', null=False, on_delete=models.PROTECT)
    from_institute = models.ForeignKey(Institute, verbose_name='Отправитель', on_delete=models.PROTECT, related_name = 'institute_from')
    to_institute = models.ForeignKey(Institute, verbose_name='Получатель', on_delete=models.PROTECT,  related_name = 'institute_to')
    document_type = models.ForeignKey(DocumentTypes, verbose_name = 'Тип документа',  on_delete=models.PROTECT)
    period = models.ForeignKey('Period', verbose_name='Период планирования', on_delete=models.SET_NULL, null=True, default=None)
    start_date = models.DateField(null=True, default=None)
    expiration_date = models.DateField(null=True, default=None)

    def __str__(self):
        return self.process.name
    

class UserInstitutes(HackathonBase):
    class Meta:
        db_table = 'users_institutes'
        verbose_name = u'Организации пользователя'
        verbose_name_plural = u'Организации пользователя'
    
    user = models.OneToOneField(User, verbose_name='Пользователь', on_delete=models.CASCADE, null=True)
    institutes = models.ManyToManyField('Institute', verbose_name='Доступные организации')

    def __str__(self):
        return self.user.username


class Period(HackathonDictionary):
    class Meta:
        db_table = 'periods'
        verbose_name = 'Периоды'
        verbose_name_plural = 'Периоды'
    
    start_date = models.DateField(null=True, default=None)
    expiration_date = models.DateField(null=True, default=None)

    def __str__(self):
        return self.name



