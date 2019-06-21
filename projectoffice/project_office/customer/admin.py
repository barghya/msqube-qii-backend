from django.contrib import admin
from customer.models import TblAddress, TblCommChannel, TblCustomer, TblCustomerAditionalAttribute, TblEmail, TblLegalInfo, TblPhone, TblProject, TblProjectAttributes

admin.site.register(TblAddress)
admin.site.register(TblCommChannel)
admin.site.register(TblCustomer)
admin.site.register(TblCustomerAditionalAttribute)
admin.site.register(TblEmail)
admin.site.register(TblLegalInfo)
admin.site.register(TblPhone)
admin.site.register(TblProject)
admin.site.register(TblProjectAttributes)