from django.shortcuts import render, redirect

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views import generic
from django.urls import reverse_lazy
from django.http import HttpResponse
import json

from cmp.models import Proveedor
from cmp.forms import ProveedorForm

from bases.views import SinPrivilegios
from django.contrib.auth.decorators import login_required, permission_required

class ProveedorView(SinPrivilegios, generic.ListView):
    permission_required = "cmp.view_proveedor"
    model = Proveedor
    template_name = "cmp/proveedor_lista.html"
    context_object_name = "obj"
    #login_url="bases:login"

class ProveedorNew(SuccessMessageMixin, SinPrivilegios, generic.CreateView):
    model = Proveedor
    template_name="cmp/proveedor_form.html"
    context_object_name = 'obj'
    form_class = ProveedorForm
    success_url= reverse_lazy("cmp:proveedor_lista")
    #login_url="bases:login"
    success_message = "Proveedor Creado Satisfactoriamente"
    permission_required = "cmp.add_proveedor"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        # print(self.request.user.id)
        return super().form_valid(form)

class ProveedorEdit(SuccessMessageMixin, SinPrivilegios, generic.UpdateView):
    model = Proveedor
    template_name = "cmp/proveedor_form.html"
    context_object_name = "obj"
    form_class = ProveedorForm
    success_url	= reverse_lazy("cmp:proveedor_lista")
    #login_url="bases:login"
    success_message = "Proveedor Editado"
    permission_required = "cmp.change_proveedor"
    
    def form_valid(self, form):
        form.instance.um = self.request.user.id
        print(self.request.user.id)
        return super().form_valid(form)
    
@login_required(login_url="bases:login")
@permission_required("cmp.change_proveedor", login_url="bases:sin_privilegios")
def producto_inactivar(request, id):
    proveedor = Proveedor.objects.filter(pk=id).first()
    contexto = {}
    template_name = "cmp/inactivar_prv.html"
    
    if not proveedor:
        return HttpResponse('Proveedor no existe ' + str(id))
    
    if not proveedor:
        return redirect("cmp:proveedor_lista")
    
    if request.method == "GET":
        contexto = {"obj": proveedor}
    
    if request.method == "POST":
        proveedor.estado = False
        proveedor.save()
        contexto={'obj':'OK'}
        return HttpResponse('Proveedor Inactivado')
        
    return render(request, template_name, contexto)   