from rest_framework import serializers
from .models import Merchandiser,Manager,Route

class MerchandiserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merchandiser
        fields = ('username', 'route', 'phone_number','email', 'location')

