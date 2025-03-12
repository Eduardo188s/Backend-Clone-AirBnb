from rest_framework import serializers

from .models import Property


class PropertiesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        field = (
            'id',
            'title',
            'price_per_nigth',
            'image_url'
        )