from ..models import encrypt
from rest_framework import serializers

class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = encrypt
        fields = '__all__'
        