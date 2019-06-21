from rest_framework import serializers
from .models import TblAddress, TblAditionalAttribute, TblCommChannel, TblEmail, TblLegalInfo, TblOrganization, TblPhone
from django.db import transaction
class AdditionalAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model=TblAditionalAttribute
        fields='__all__'

class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model=TblPhone
        fields='__all__'
class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model=TblAddress
        fields='__all__'

class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model=TblEmail
        fields='__all__'

class CommChannnelSerializer(serializers.ModelSerializer):
    comm_channel_phone=PhoneSerializer(source='comm_phone',many=True)
    comm_channel_email=EmailSerializer(source='comm_email',many=True)
    comm_channel_address=AddressSerializer(source='comm_address',many=True)
    class Meta:
        model=TblCommChannel
        fields='__all__'


class LegalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model=TblLegalInfo
        fields='__all__'


class OrgSerializer(serializers.ModelSerializer):
    additional_attributes=AdditionalAttributeSerializer(source='additional_att',many=True)
    comm_attribute=CommChannnelSerializer(source='comm_chnl',many=True)
    org_legalinfo=LegalInfoSerializer(source='org_legal_info',many=True)
    class Meta:
        model=TblOrganization
        fields='__all__'
    
