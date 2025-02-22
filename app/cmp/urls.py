from django.urls import path

from cmp.views import ProveedorView, ProveedorNew, ProveedorEdit, producto_inactivar, ComprasView, compras, CompraDetDelete

urlpatterns = [
    path('proveedor/', ProveedorView.as_view(), name='proveedor_lista'),
    path('proveedor/new', ProveedorNew.as_view(), name='proveedor_new'),
    path('proveedor/edit/<int:pk>', ProveedorEdit.as_view(), name='proveedor_edit'),
    path('proveedor/inactivar/<int:id>', producto_inactivar, name='proveedor_inactivar'),
    
    path('compras/', ComprasView.as_view(), name='compras_lista'),
    path('compras/new', compras, name='compras_new'),
    path('compras/edit/<int:compra_id>', compras, name='compras_edit'),
    path('compras/<int:compra_id>/delete/<int:pk>', CompraDetDelete.as_view(), name='compras_del'),
]