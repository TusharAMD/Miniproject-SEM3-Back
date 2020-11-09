from ..models import decrypt
from rest_framework import serializers

class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = decrypt
        fields = '__all__'
        