# -*- coding: utf-8 -*-
from django.db.models import Q, Max, Count
from django.contrib import auth

from rest_framework import generics, permissions
from django_filters import rest_framework as filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.mixins import DestroyModelMixin
from rest_framework.pagination import PageNumberPagination
from rest_framework.exceptions import NotFound, bad_request
from rest_framework.exceptions import AuthenticationFailed
from django.shortcuts import get_object_or_404, get_list_or_404, redirect
from django.utils import timezone
from django.urls import reverse
from django.db.models import Q
#import requests

from .serializers import *
from hackathon.models import *

def get_nested_institutes(user):
      set_institutes = set()
      query_set = UserInstituntesView.queryset.filter(user=user)
      for _ in query_set:
          for institute in _.institutes.all():
              while institute is not None:
                  set_institutes.add(institute)
                  institute = institute.founder
      return list(set_institutes)


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 30
    page_size_query_param = 'page_size'


class MaxResultsSetPagination(PageNumberPagination):
    page_size = 1000
    page_size_query_param = 'page_size'


class DocumentTypeList(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = DocumentTypeSerializer

    def get_queryset(self):
        return DocumentTypes.objects.all()

class UserInstituntesView(generics.RetrieveAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserInstitutesSerializer
    lookup_field = 'user__pk'
    queryset = UserInstitutes.objects.all()


class ProcessListView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = ProcessSerializer

    def get_queryset(self):
        institutes = get_nested_institutes(self.request.user)
        processes = Process.objects.filter(Q(from_institute__in=institutes) | 
                               Q(to_institute__in=institutes))
        return processes
       


   

        
