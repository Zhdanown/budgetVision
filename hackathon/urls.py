# -*- coding: utf-8 -*-
from datetime import datetime
from django.contrib import admin
from django.conf.urls import url,include
from django.conf.urls.static import static
from django.conf import settings
import django.contrib.auth.views
from hackathon.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='home'),
]
