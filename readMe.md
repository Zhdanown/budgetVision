# B-vision

Визуализатор бюджетных процессов г. Москва

***
## Стэк используемых технологий
>Python 3, 
>Django 2.1.7 
>>  requirements:
>>>		Django
>>>		psycopg2
>>>		django-rest-framefork
>>>		django-allauth
>>>		django-filters
>СУБД: Postgres SQL 10
>FRONT END: Material, AngularJS

***
### Структура проекта
> HACKATHON (Django Приложение)
>>  api (RestAPI)
>>>		views.py (api методы)
>>>		urls.py (маршрутизация)
>>>		serializers.py (Классы сериализаторы для моделей данных проекта)
>>  api (RestAPI)
>>>		js/app/ (Angular JS приложение)
>>  css (Стили на material)
>>  templates (HTML Шаблоны страниц. Реализовано через layout и views)
>>>		account (Раширили шаблоны allauth)
>>  admin.py (файл настройки панели администратора)
>>  models.py (файл моделей данных)
>>  settings.py (настройки проекта)
>>  views.py (представления данных)
>>  urls.py (настройки маршрутизации проектов)
