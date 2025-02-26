from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse

from datetime import datetime

from bases.views import SinPrivilegios
from fac.models import Cliente, FacturaEnc, FacturaDet
from fac.forms import ClienteForm
import inv.views as inv


class ClienteView(SinPrivilegios, generic.ListView):
    permission_required = "fac.view_cliente"
    model = Cliente
    template_name = "fac/clientes_lista.html"
    context_object_name = "obj"

class VistaBaseCreate(SuccessMessageMixin, SinPrivilegios, generic.CreateView):
    context_object_name = "obj"
    success_message = "Registro Agregado Satisfactoriamente"
    
    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class VistaBaseEdit(SuccessMessageMixin, SinPrivilegios, generic.UpdateView):
    context_object_name = "obj"
    success_message = "Registro Actualizado Satisfactoriamente"
    
    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

class ClienteNew(VistaBaseCreate):
    model = Cliente
    form_class = ClienteForm
    template_name="fac/cliente_form.html"
    permission_required = "fac.add_cliente"
    success_url= reverse_lazy("fac:cliente_lista")

class ClienteEdit(VistaBaseEdit):
    model = Cliente
    form_class = ClienteForm
    template_name="fac/cliente_form.html"
    permission_required = "fac.change_cliente"
    success_url= reverse_lazy("fac:cliente_lista")

@login_required(login_url="bases:login")
@permission_required("fact.change_cliente", login_url="bases:sin_privilegios")
def clienteInactivar(request, id):
    cliente = Cliente.objects.filter(pk=id).first()
    
    if request.method == "POST":
        if cliente:
            cliente.estado = not cliente.estado
            cliente.save()
            return HttpResponse("OK")
        return HttpResponse("FAIL")

    return HttpResponse("FAIL")

class FacturaView(SinPrivilegios, generic.ListView):
    model = FacturaEnc
    template_name = "fac/factura_lista.html"
    context_object_name = "obj"
    permission_required="fac.view_facturaenc"

@login_required(login_url='bases:login')
@permission_required('fac.change_facturaenc', login_url='bases:sin_privilegios')
def facturas(request,id=None):
    template_name='fac/facturas.html'
    
    encabezado = {
        "fecha": datetime.today()
    }
    detalle = {}
    clientes = Cliente.objects.filter(estado=True)
    contexto = {
        "enc": encabezado,
        "det": detalle,
        "clientes": clientes
    }
    
    
    
    return render(request, template_name, contexto)

class ProductoView(inv.ProductoView):
    template_name = "fac/buscar_producto.html"
    
