from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from django.views import generic
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required, permission_required

from inv.models import Categoria, SubCategoria, Marca, UnidadMedida, Producto
from inv.forms import CategoriaForm, SubCategoriaForm, MarcaForm, UMForm, ProductoForm

from bases.views import SinPrivilegios

class CategoriaView(SinPrivilegios, generic.ListView):
    permission_required = "inv.view_categoria"
    model = Categoria
    template_name = "inv/categoria_lista.html"
    context_object_name = "obj"
    #login_url="bases:login"

class CategoriaNew(SuccessMessageMixin, SinPrivilegios, generic.CreateView):
    model = Categoria
    template_name = "inv/categoria_form.html"
    context_object_name = "obj"
    form_class = CategoriaForm
    success_url	= reverse_lazy("inv:categoria_lista")
    #login_url="bases:login"
    success_message = "Categoría Creada Satisfactoriamente"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class CategoriaEdit(SuccessMessageMixin, LoginRequiredMixin, generic.UpdateView):
    model = Categoria
    template_name = "inv/categoria_form.html"
    context_object_name = "obj"
    form_class = CategoriaForm
    success_url	= reverse_lazy("inv:categoria_lista")
    login_url = "bases:login"
    success_message = "Categoría Actualizada Satisfactoriamente"
    
    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

class CategoriaDelete(LoginRequiredMixin, generic.DeleteView):
    model = Categoria
    template_name = "inv/categoria_delete.html"
    context_object_name = "obj"
    success_url	= reverse_lazy("inv:categoria_lista")
    success_message = "Categoría Eliminada Satisfactoriamente"

class SubCategoriaView(SinPrivilegios, generic.ListView):
    permission_required = "inv.view_subcategoria"
    model = SubCategoria
    template_name = "inv/subcategoria_lista.html"
    context_object_name = "obj"
    #login_url = 'bases:login'
    """
    def handle_no_permission(self): # this can be used to redirect to a 404/403 forbidden page 
        if self.request.user.is_authenticated:
            return render(self.request, "bases/403.html", status=403)
        else:
            return redirect(self.get_login_url())
    """


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

class MarcaView(SinPrivilegios, generic.ListView):
    permission_required = "inv.view_marca"
    model = Marca
    template_name = "inv/marca_lista.html"
    context_object_name = "obj"
    #login_url = "bases:login"
    
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

@login_required(login_url="bases:login")
@permission_required("inv.change_marca", login_url="bases:sin_privilegios")
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
        messages.success(request, 'Marca {} Inactivada'.format(marca.descripcion)) # esto ayuda en la plantilla base.html en mensaje("{{ message }}", "{{ message.tags }}"); para mandar un model jquery en la pantalla
        # messages.success(request, 'Marca {} Inactivada'.format(marca.descripcion), "red") # puedes poner el color que quieres 
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
    
    def get_context_data(self, **kwargs):
        context = super(ProductoNew, self).get_context_data(**kwargs)
        context["categorias"] = Categoria.objects.all()
        context["subcategorias"] = SubCategoria.objects.all()
        return context

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