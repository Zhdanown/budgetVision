from django.conf.urls import url
from hackathon.api.views import *

urlpatterns = [    
    url(r'^document-types/$', DocumentTypeList.as_view()),
]