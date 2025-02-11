from django.shortcuts import render, redirect

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from inv.models import Categoria, SubCategoria, Marca, UnidadMedida, Producto
from inv.forms import CategoriaForm, SubCategoriaForm, MarcaForm, UMForm, ProductoForm

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
    login_url="bases:login"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class CategoriaEdit(LoginRequiredMixin, generic.UpdateView):
    model = Categoria
    template_name = "inv/categoria_form.html"
    context_object_name = "obj"
    form_class = CategoriaForm
    success_url	= reverse_lazy("inv:categoria_lista")
    login_url = "bases:login"
    
    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

class CategoriaDelete(LoginRequiredMixin, generic.DeleteView):
    model = Categoria
    template_name = "inv/categoria_delete.html"
    context_object_name = "obj"
    success_url	= reverse_lazy("inv:categoria_lista")
    success_message = "Categoría Eliminada Satisfactoriamente"

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
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class SubCategoriaEdit(LoginRequiredMixin, generic.UpdateView):
    model = SubCategoria
    template_name = "inv/subcategoria_form.html"
    context_object_name = "obj"
    form_class = SubCategoriaForm
    success_url	= reverse_lazy("inv:subcategoria_lista")
    login_url = "bases:login"
    
    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

class SubCategoriaDelete(LoginRequiredMixin, generic.DeleteView):
    model = SubCategoria
    template_name = "inv/categoria_delete.html"
    context_object_name = "obj"
    success_url	= reverse_lazy("inv:subcategoria_lista")
    success_message = "Categoría Eliminada Satisfactoriamente"

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
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class MarcaEdit(LoginRequiredMixin, generic.UpdateView):
    model = Marca
    template_name = "inv/marca_form.html"
    context_object_name = "obj"
    form_class = MarcaForm
    success_url	= reverse_lazy("inv:marca_lista")
    login_url = "bases:login"
    
    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

def marca_inactivar(request, id):
    marca = Marca.objects.filter(pk=id).first()
    contexto = {}
    template_name = "inv/categoria_delete.html"
    
    if not marca:
        return redirect("inv:marca_lista")
    
    if request.method == "GET":
        contexto = {"obj": marca}
    
    if request.method == "POST":
        marca.estado = False
        marca.save()
        return redirect("inv:marca_lista")
        
    return render(request, template_name, contexto)    

class UMView(LoginRequiredMixin, generic.ListView):
    model = UnidadMedida
    template_name = "inv/um_lista.html"
    context_object_name = "obj"
    login_url = "bases:login"
    
class UMNew(LoginRequiredMixin, generic.CreateView):
    model = UnidadMedida
    template_name="inv/um_form.html"
    context_object_name = 'obj'
    form_class=UMForm
    success_url= reverse_lazy("inv:um_lista")
    login_url="bases:login"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        print(self.request.user.id)
        return super().form_valid(form)

class UMEdit(LoginRequiredMixin, generic.UpdateView):
    model = UnidadMedida
    template_name = "inv/um_form.html"
    context_object_name = "obj"
    form_class = UMForm
    success_url	= reverse_lazy("inv:um_lista")
    login_url="bases:login"
    
    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

def um_inactivar(request, id):
    um = UnidadMedida.objects.filter(pk=id).first()
    contexto = {}
    template_name = "inv/categoria_delete.html"
    
    if not um:
        return redirect("inv:um_lista")
    
    if request.method == "GET":
        contexto = {"obj": um}
    
    if request.method == "POST":
        um.estado = False
        um.save()
        return redirect("inv:um_lista")
        
    return render(request, template_name, contexto)   

class ProductoView(LoginRequiredMixin, generic.ListView):
    model = Producto
    template_name = "inv/producto_lista.html"
    context_object_name = "obj"
    login_url = "bases:login"

class ProductoNew(LoginRequiredMixin, generic.CreateView):
    model = Producto
    template_name="inv/producto_form.html"
    context_object_name = 'obj'
    form_class = ProductoForm
    success_url= reverse_lazy("inv:producto_lista")
    login_url="bases:login"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        # print(self.request.user.id)
        return super().form_valid(form)
    
class ProductoEdit(LoginRequiredMixin, generic.UpdateView):
    model = Producto
    template_name = "inv/producto_form.html"
    context_object_name = "obj"
    form_class = ProductoForm
    success_url	= reverse_lazy("inv:producto_lista")
    login_url="bases:login"
    
    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

def producto_inactivar(request, id):
    producto = Producto.objects.filter(pk=id).first()
    contexto = {}
    template_name = "inv/categoria_delete.html"
    
    if not producto:
        return redirect("inv:producto_lista")
    
    if request.method == "GET":
        contexto = {"obj": producto}
    
    if request.method == "POST":
        producto.estado = False
        producto.save()
        return redirect("inv:producto_lista")
        
    return render(request, template_name, contexto)   