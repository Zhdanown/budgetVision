# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .models import *

# Register your models here.
admin.site.register(DocumentTypes)
admin.site.register(Document)
admin.site.register(Institute)
#admin.site.register(Founder)
admin.site.register(BaseProcess)
admin.site.register(Process)
admin.site.register(UserInstitutes)