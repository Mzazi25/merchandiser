from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import  Merchandiser,Manager,Route,Comment
from .serializer import MerchandiserSerializer,ManagerSerializer,RouteSerializer
from rest_framework import status
from .permissions import IsAdminOrReadOnly

# Create your views here.

class MerchandiserList(APIView):
    def get(self, request, format=None):
        merch = Merchandiser.objects.all()
        serializers = MerchandiserSerializer(merch, many=True)
        return Response(serializers.data)
    def post(self, request, format=None):
        serializers = MerchandiserSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    permission_classes = (IsAdminOrReadOnly,)

class ManagerList(APIView):
    def get(self, request, format=None):
        manager = Manager.objects.all()
        serializers = ManagerSerializer(manager, many=True)
        return Response(serializers.data)
    def post(self, request, format=None):
        serializers = ManagerSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    permission_classes = (IsAdminOrReadOnly,)

class RouteList(APIView):
    def get(self, request, format=None):
        manager = Manager.objects.all()
        serializers = ManagerSerializer(manager, many=True)
        return Response(serializers.data)
    def post(self, request, format=None):
        serializers = ManagerSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    permission_classes = (IsAdminOrReadOnly,)
