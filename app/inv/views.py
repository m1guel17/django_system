from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from inv.models import Categoria, SubCategoria, Marca
from inv.forms import CategoriaForm, SubCategoriaForm, MarcaForm

class CategoriaView(LoginRequiredMixin, generic.ListView):
    model = Categoria
    template_name = "inv/categoria_lista.html"
    context_object_name = "obj"
    login_url = 'bases:login'

class CategoriaNew(LoginRequiredMixin, generic.CreateView):
    model = Categoria
    template_name = "inv/categoria_form.html"
    context_object_name = "obj"
    form_class = CategoriaForm
    success_url	= reverse_lazy("inv:categoria_lista")
    login_url="base:login"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class CategoriaEdit(LoginRequiredMixin, generic.UpdateView):
    model = Categoria
    template_name = "inv/categoria_form.html"
    context_object_name = "obj"
    form_class = CategoriaForm
    success_url	= reverse_lazy("inv:categoria_lista")
    login_url="base:login"
    
    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

class CategoriaDelete(LoginRequiredMixin, generic.DeleteView):
    model = Categoria
    template_name = "inv/categoria_delete.html"
    context_object_name = "obj"
    success_url	= reverse_lazy("inv:categoria_lista")
    success_message="Categoría Eliminada Satisfactoriamente"

class SubCategoriaView(LoginRequiredMixin, generic.ListView):
    model = SubCategoria
    template_name = "inv/subcategoria_lista.html"
    context_object_name = "obj"
    login_url = 'bases:login'

class SubCategoriaNew(LoginRequiredMixin, generic.CreateView):
    model = SubCategoria
    template_name = "inv/subcategoria_form.html"
    context_object_name = "obj"
    form_class = SubCategoriaForm
    success_url	= reverse_lazy("inv:subcategoria_lista")
    login_url="base:login"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class SubCategoriaEdit(LoginRequiredMixin, generic.UpdateView):
    model = SubCategoria
    template_name = "inv/subcategoria_form.html"
    context_object_name = "obj"
    form_class = SubCategoriaForm
    success_url	= reverse_lazy("inv:subcategoria_lista")
    login_url="base:login"
    
    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

class SubCategoriaDelete(LoginRequiredMixin, generic.DeleteView):
    model = SubCategoria
    template_name = "inv/categoria_delete.html"
    context_object_name = "obj"
    success_url	= reverse_lazy("inv:subcategoria_lista")
    success_message="Categoría Eliminada Satisfactoriamente"

class MarcaView(LoginRequiredMixin, generic.ListView):
    model = Marca
    template_name = "inv/marca_lista.html"
    context_object_name = "obj"
    login_url = "bases:login"
    
class MarcaNew(LoginRequiredMixin, generic.CreateView):
    model = Marca
    template_name = "inv/marca_form.html"
    context_object_name = "obj"
    form_class = MarcaForm
    success_url	= reverse_lazy("inv:marca_lista")
    login_url="base:login"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class MarcaEdit(LoginRequiredMixin, generic.UpdateView):
    model = Marca
    template_name = "inv/marca_form.html"
    context_object_name = "obj"
    form_class = MarcaForm
    success_url	= reverse_lazy("inv:marca_lista")
    login_url="base:login"
    
    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

