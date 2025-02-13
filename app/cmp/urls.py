from django.urls import path

from cmp.views import ProveedorView, ProveedorNew, ProveedorEdit, producto_inactivar

urlpatterns = [
    path('proveedor/', ProveedorView.as_view(), name='proveedor_lista'),
    path('proveedor/new', ProveedorNew.as_view(), name='proveedor_new'),
    path('proveedor/edit/<int:pk>', ProveedorEdit.as_view(), name='proveedor_edit'),
    path('proveedor/inactivar/<int:id>', producto_inactivar, name='proveedor_inactivar'),
    
]