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
from django.shortcuts import get_object_or_404, redirect
from django.utils import timezone
from django.urls import reverse
from django.db.models import Q
import requests

from .serializers import *
from hackathon.models import *


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
