from rest_framework import serializers
from .models import Merchandiser,Manager,Address

class MerchandiserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merchandiser
        fields = ('username', 'phone_number','email', 'location')

class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = ('name', 'description', 'phone_number', 'location')

class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('city', 'location')
