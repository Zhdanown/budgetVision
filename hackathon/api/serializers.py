from rest_framework import serializers
import json

from hackathon.models import *


class DocumentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentTypes
        fields = '__all__'


class UserInstitutesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInstitutes
        fields = '__all__'
