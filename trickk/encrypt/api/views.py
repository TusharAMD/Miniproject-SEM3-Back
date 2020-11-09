from rest_framework import viewsets
from .serializers import ImageSerializer
from ..models import encrypt

class ImageViewSet(viewsets.ModelViewSet):
    queryset = encrypt.objects.all().order_by('-uploaded')
    serializer_class = ImageSerializer