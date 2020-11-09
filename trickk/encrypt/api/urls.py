from .views import ImageViewSet
from rest_framework import routers
from django.urls import path, include

app_name = 'api-encrypt'

router = routers.DefaultRouter()
router.register(r'encrypt', ImageViewSet)

urlpatterns = [
    path('', include(router.urls))
]
