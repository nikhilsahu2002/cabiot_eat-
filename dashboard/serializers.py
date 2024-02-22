from rest_framework import serializers
from .models import Kitchen, Menu, MenuItem, DeliveryArea

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'menu', 'name', 'description', 'price', 'image', 'status', 'calories']

class MenuSerializer(serializers.ModelSerializer):
    items = MenuItemSerializer(many=True, read_only=True)
    
    class Meta:
        model = Menu
        fields = ['id', 'kitchen','name', 'description', 'image', 'created_at','status', 'items']

class KitchenSerializer(serializers.ModelSerializer):
    menu = MenuSerializer(read_only=True)

    class Meta:
        model = Kitchen
        fields = ['id', 'name', 'location', 'is_delivery_available', 'menu']

class DeliveryAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryArea
        fields = ['id', 'area_name','kitchen']
