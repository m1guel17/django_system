from django.urls import path

from fac.views import ClienteView, ClienteNew, ClienteEdit, clienteInactivar, FacturaView, facturas, ProductoView, borrar_detalle_factura

urlpatterns = [
    path('clientes/', ClienteView.as_view(), name='cliente_lista'),
    path('clientes/new', ClienteNew.as_view(), name='cliente_new'),
    path('clientes/<int:pk>', ClienteEdit.as_view(), name='cliente_edit'),
    path('clientes/estado/<int:id>', clienteInactivar, name='cliente_inactivar'),
    
    path('facturas/', FacturaView.as_view(), name='facturas_lista'),
    path('facturas/news', facturas, name='factura_new'),
    path('facturas/edit/<int:id>', facturas, name='factura_edit'),
    path('facturas/buscar-producto', ProductoView.as_view(), name='factura_producto'),
    
    path('facturas/borrar-detalle/<int:id>', borrar_detalle_factura, name='factura_borrar_detalle'),
    
]