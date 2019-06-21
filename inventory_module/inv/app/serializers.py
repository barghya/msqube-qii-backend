from rest_framework import serializers
from .models import materialmaster, materialunit

class matunitSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = materialunit
        fields = '__all__'

class matmasterSerializer(serializers.ModelSerializer):
    material_unit_set = matunitSerializer(source='mat_unit',many=True,read_only=True)
    class Meta:
        model = materialmaster
        fields = '__all__'

