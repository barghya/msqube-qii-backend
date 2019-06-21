from django.conf.urls import include, url
try:
  from django.conf.urls import patterns
except ImportError:
  pass
import django
from django.contrib import admin
from django.urls import path
from customer import views
from rest_framework import routers

urlpatterns = [
  
    url(r'^tbladdress/(?P<id>[0-9]+)$', views.TblAddressAPIView.as_view()),
    url(r'^tbladdress/$', views.TblAddressAPIListView.as_view()),
  
    url(r'^tblcommchannel/(?P<id>[0-9]+)$', views.TblCommChannelAPIView.as_view()),
    url(r'^tblcommchannel/$', views.TblCommChannelAPIListView.as_view()),
  
    url(r'^tblcustomer/(?P<id>[0-9]+)$', views.TblCustomerAPIView.as_view()),
    url(r'^tblcustomer/$', views.TblCustomerAPIListView.as_view()),
  
    url(r'^tblcustomeraditionalattribute/(?P<id>[0-9]+)$', views.TblCustomerAditionalAttributeAPIView.as_view()),
    url(r'^tblcustomeraditionalattribute/$', views.TblCustomerAditionalAttributeAPIListView.as_view()),
  
    url(r'^tblemail/(?P<id>[0-9]+)$', views.TblEmailAPIView.as_view()),
    url(r'^tblemail/$', views.TblEmailAPIListView.as_view()),
  
    url(r'^tbllegalinfo/(?P<id>[0-9]+)$', views.TblLegalInfoAPIView.as_view()),
    url(r'^tbllegalinfo/$', views.TblLegalInfoAPIListView.as_view()),
  
    url(r'^tblphone/(?P<id>[0-9]+)$', views.TblPhoneAPIView.as_view()),
    url(r'^tblphone/$', views.TblPhoneAPIListView.as_view()),
  
    url(r'^tblproject/(?P<id>[0-9]+)$', views.TblProjectAPIView.as_view()),
    url(r'^tblproject/$', views.TblProjectAPIListView.as_view()),
  
    url(r'^tblprojectattributes/(?P<id>[0-9]+)$', views.TblProjectAttributesAPIView.as_view()),
    url(r'^tblprojectattributes/$', views.TblProjectAttributesAPIListView.as_view()),
	

  
  ]
