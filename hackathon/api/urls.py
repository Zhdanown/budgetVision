from django.conf.urls import url
from hackathon.api.views import *

urlpatterns = [    
    url(r'^document-types/$', DocumentTypeList.as_view()),
    url(r'^user/(?P<user__pk>\d+)/$', UserInstituntes.as_view()),
]