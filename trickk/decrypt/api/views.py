from rest_framework import viewsets
from .serializers import ImageSerializer
from ..models import decrypt

class ImageViewSet(viewsets.ModelViewSet):
    queryset = decrypt.objects.all().order_by('-uploaded')
    serializer_class = ImageSerializer