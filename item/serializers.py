from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'item_image', 'name', 'slug', 'type', 'item_status', 'color', 'available']
