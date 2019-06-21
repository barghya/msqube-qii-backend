
from django.urls import path,include
from rest_framework import routers
from .views import *

router=routers.DefaultRouter()
router.register(r'/unit',matunitViewset)
router.register(r'/master',matmasterViewset)
urlpatterns = [
    path('materials',include(router.urls)),
]
