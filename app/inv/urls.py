from django.urls import path

from inv.views import CategoriaView, CategoriaNew, CategoriaEdit, CategoriaDelete, SubCategoriaView, SubCategoriaNew, SubCategoriaEdit, SubCategoriaDelete, MarcaView, MarcaNew, MarcaEdit

urlpatterns = [
    path('categorias/', CategoriaView.as_view(), name='categoria_lista'),
    path('categorias/new', CategoriaNew.as_view(), name='categoria_new'),
    path('categorias/edit/<int:pk>', CategoriaEdit.as_view(), name='categoria_edit'),
    path('categorias/delete/<int:pk>', CategoriaDelete.as_view(), name='categoria_del'),
    
    path('subcategorias/', SubCategoriaView.as_view(), name='subcategoria_lista'),
    path('subcategorias/new', SubCategoriaNew.as_view(), name='subcategoria_new'),
    path('subcategorias/edit/<int:pk>', SubCategoriaEdit.as_view(), name='subcategoria_edit'),
    path('subcategorias/delete/<int:pk>', SubCategoriaDelete.as_view(), name='subcategoria_del'),
    
    path('marcas/', MarcaView.as_view(), name='marca_lista'),
    path('marcas/new', MarcaNew.as_view(), name='marca_new'),
    path('marcas/edit/<int:pk>', MarcaEdit.as_view(), name='marca_edit'),
]
