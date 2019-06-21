from django.urls import path,include
from rest_framework import routers
from .import views
router=routers.DefaultRouter()
router.register(r'organizations',views.orgViewSet)
#router.register(r'add_attribute',views.attributeViewSet)
#router.register(r'comm_attribute',views.commViewSet)
#router.register(r'comm_phone',views.phoneViewSet)
#router.register(r'comm_address',views.addressViewSet)
#router.register(r'comm_email',views.emailViewSet)
#router.register(r'legal_attribute',views.legalViewSet)
urlpatterns = [

    path('',include(router.urls)),
]
