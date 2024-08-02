from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .product import products

# Create your views here.

@api_view(['GET'])
def get_message(request):
 return Response("Hello Lokesh")

@api_view(['GET'])
def get_products(request):
 return Response(products)