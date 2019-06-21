from django.forms import forms
from rest_framework import viewsets, request
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework.utils import json

from .models import materialmaster, materialunit
from .serializers import matmasterSerializer, matunitSerializer

class matmasterViewset(viewsets.ModelViewSet):
    queryset=materialmaster.objects.all()
    serializer_class=matmasterSerializer
class matunitViewset(viewsets.ModelViewSet):
    queryset=materialunit.objects.all()
    serializer_class=matunitSerializer

@api_view(['GET','POST'])
def material_listing(request, format=None):
           
    if request.method == 'POST':
        serializer=matmasterSerializer(data=request.data)
        print("ok")
        serializer.save()