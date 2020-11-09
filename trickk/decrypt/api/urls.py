from .views import ImageViewSet
from rest_framework import routers
from django.urls import path, include

app_name = 'api-decrypt'

router = routers.DefaultRouter()
router.register(r'decrypt', ImageViewSet)

urlpatterns = [
    path('', include(router.urls))
]
