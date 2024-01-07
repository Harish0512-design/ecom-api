from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Order
from .serializers import OrderSerializer


# Create your views here.

class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
