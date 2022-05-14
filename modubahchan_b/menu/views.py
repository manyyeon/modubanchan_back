from telnetlib import STATUS
from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from .models import *
# Create your views here.

@api_view(['GET','POST'])
def product_list_create(request):
    if request.method == 'GET':
        menus = Product.objects.all()
        serializer = ProductListSerializer(menus, many=True)
        return Response(data=serializer.data)

    if request.method == 'POST':
        serializer = ProductListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data,status=STATUS.HTTP_201_CREATED)
    
@api_view(['GET','DELETE','PUT'])
def product_detail_update_delete(request,product_pk):
    product = get_object_or_404(Product, pk=product_pk)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        product.delete()
        data={
            'product_pk':product_pk
        }
        return Response(data,status=STATUS.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = ProductSerializer(instance=product, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
