from django.urls import path

from api.views import ProductoList, ProductoDetalle

urlpatterns = [
    path('v1/productos/', ProductoList.as_view(), name='producto_list'),
    path('v1/productos/<str:codigo>', ProductoDetalle.as_view(), name='producto_detalle'),
]
