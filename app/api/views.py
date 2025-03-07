from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from rest_framework.views import APIView
from rest_framework.response import Response

from api.serializers import ProductoSerializer
from inv.models import Producto

class ProductoList(APIView):
    def get(self, request):
        prod = Producto.objects.all()
        data = ProductoSerializer(prod, many=True).data
        
        return Response(data)
    
class ProductoDetalle(APIView):
    def get(self, request, codigo):
        # prod = get_object_or_404(Producto, codigo=codigo)
        prod = get_object_or_404(Producto, Q(codigo=codigo)|Q(codigo_barra=codigo))
        data = ProductoSerializer(prod).data
        
        return Response(data)
        