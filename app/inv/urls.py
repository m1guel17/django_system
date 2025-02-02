from django.urls import path

from inv.views import CategoriaView, CategoriaNew, CategoriaEdit, CategoriaDelete

urlpatterns = [
    path('categorias/', CategoriaView.as_view(), name='categoria_lista'),
    path('categorias/new', CategoriaNew.as_view(), name='categoria_new'),
    path('categorias/edit/<int:pk>', CategoriaEdit.as_view(), name='categoria_edit'),
    path('categorias/delete/<int:pk>', CategoriaDelete.as_view(), name='categoria_del'),
]
