from rest_framework import serializers
from .models import Url

class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields = '__all__'

    def create(self, validated_data):
        short_url = Url.generate_short_url()
        return Url.objects.create(short_url=short_url, **validated_data)
