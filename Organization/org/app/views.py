from django.forms import forms
from rest_framework import viewsets, request
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework.utils import json
from .models import TblAddress, TblAditionalAttribute, TblCommChannel, TblEmail, TblLegalInfo, TblOrganization, TblPhone
from .serializers import OrgSerializer,AdditionalAttributeSerializer,LegalInfoSerializer,CommChannnelSerializer,AddressSerializer,PhoneSerializer,EmailSerializer
# Create your views here.

class orgViewSet(viewsets.ModelViewSet):
    queryset=TblOrganization.objects.all()
    serializer_class = OrgSerializer

class addressViewSet(viewsets.ModelViewSet):
    queryset=TblAddress.objects.all()
    serializer_class = AddressSerializer

class attributeViewSet(viewsets.ModelViewSet):
    queryset=TblAditionalAttribute.objects.all()
    serializer_class = AdditionalAttributeSerializer

class legalViewSet(viewsets.ModelViewSet):
    queryset=TblLegalInfo.objects.all()
    serializer_class = LegalInfoSerializer

class commViewSet(viewsets.ModelViewSet):
    queryset=TblCommChannel.objects.all()
    serializer_class = CommChannnelSerializer

class emailViewSet(viewsets.ModelViewSet):
    queryset=TblEmail.objects.all()
    serializer_class = EmailSerializer

class phoneViewSet(viewsets.ModelViewSet):
    queryset=TblPhone.objects.all()
    serializer_class = PhoneSerializer