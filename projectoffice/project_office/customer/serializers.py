from rest_framework.serializers import ModelSerializer
from customer.models import TblAddress, TblCommChannel, TblCustomer, TblCustomerAditionalAttribute, TblEmail, TblLegalInfo, TblPhone, TblProject, TblProjectAttributes


class TblAddressSerializer(ModelSerializer):
	
    class Meta:
        model = TblAddress
        fields = '__all__'

class TblLegalInfoSerializer(ModelSerializer):
	
    class Meta:
        model = TblLegalInfo
        fields = '__all__'
		



class TblCommChannelSerializer(ModelSerializer):

    class Meta:
        model = TblCommChannel
        fields = '__all__'


class TblCustomerSerializer(ModelSerializer):
	cust_ref=TblCommChannelSerializer(many=True);
	
	class Meta:
		model = TblCustomer
		fields = '__all__'



class TblCustomerAditionalAttributeSerializer(ModelSerializer):

    class Meta:
        model = TblCustomerAditionalAttribute
        fields = '__all__'


class TblEmailSerializer(ModelSerializer):

    class Meta:
        model = TblEmail
        fields = '__all__'



class TblPhoneSerializer(ModelSerializer):

    class Meta:
        model = TblPhone
        fields = '__all__'


class TblProjectSerializer(ModelSerializer):

    class Meta:
        model = TblProject
        fields = '__all__'


class TblProjectAttributesSerializer(ModelSerializer):

    class Meta:
        model = TblProjectAttributes
        fields = '__all__'

class customerdetserializer(ModelSerializer):
	#customers=TblCustomerSerializer(source='tbl_customer',many=True)
	addresses=TblAddressSerializer(source='TblAddress',many=True)
	class Meta:
		model=TblCustomer,
		fields='__all__'