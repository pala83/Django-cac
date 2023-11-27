from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from .forms import ContactoForm, AltaCervezaModelForm, AltaProovedorModelForm, AltaIngresoInsumosModelForm
from .models import Cerveza, IngresoInsumos, Proovedor

def index(request):
    logos = [
        '01-kolsch.png',
        '02-irish-stout.png',
        '03-altbier.png',
        '04-stolichno.png',
        '05-pilsener.png',
        '06-guinnes.png',
        '07-camdem-pale-ale.png',
        '08-ipa-green.png',
        '09-smithwicks.png',
        '10-dunkel.png',
        '11-pillus.png',
        '12-old-vienna.png',
        '13-barley.png',
        '14-black-scottish-stout.png',
        '15-kostriber.png',
        '16-london-porter.png',
    ]

    context = {
        'logos': logos
    }
    return render(request, "core/index.html", context)

def cervezas(request):
    listado = Cerveza.objects.all().order_by('tipo')

    context = {
        'tipos': ['rubia', 'roja', 'negra'],
        'lista': listado
        }
    return render(request, "core/cervezas.html", context)

def contacto(request):
    print(request.POST)
    if request.method == "POST":
        formulario = ContactoForm(request.POST)
        if formulario.is_valid():
            messages.info(request, "Su consulta fue enviada con exito.")
            return redirect(reverse("index"))
    else:
        formulario = ContactoForm()
    context ={
        'contacto_form': formulario
    }
    return render(request, "core/contacto.html", context)

class ProovedoresView(LoginRequiredMixin, TemplateView):
    template_name = "core/proovedores.html"
    login_url ="/proovedores/login"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["proovedores"] = Proovedor.objects.all()
        return context
    
    def get_insumo_detalle(self, request, id_proovedor):
        try:
            insumos = IngresoInsumos.objects.filter(proovedor__id=id_proovedor)
        except IngresoInsumos.DoesNotExist:
            return None
        context = {'insumos': insumos,
                   'proovedores': Proovedor.objects.all(),
                   'id_actual': id_proovedor}
        return render(request, 'core/proovedores.html', context)

    def get(self, request, *args, **kwargs):
        id_proovedor = kwargs.get('id_proovedor')
        if id_proovedor:
            return self.get_insumo_detalle(request, id_proovedor)
        else:
            return super().get(request, *args, *kwargs)
    
class CervezaCreateView(LoginRequiredMixin, CreateView):
    model = Cerveza
    template_name = "core/alta_cerveza.html"
    form_class = AltaCervezaModelForm
    success_url = reverse_lazy('proovedores')

    def form_valid(self, form):
        form.instance.cliente = self.request.user
        return super().form_valid(form)
    
class ProovedorCreateView(LoginRequiredMixin, CreateView):
    model = Proovedor
    template_name = "core/alta_proovedor.html"
    form_class = AltaProovedorModelForm
    success_url = reverse_lazy('proovedores')

    def form_valid(self, form):
        form.instance.cliente = self.request.user
        return super().form_valid(form)
    
class IngresoInsumosCreateView(LoginRequiredMixin, CreateView):
    model = IngresoInsumos
    form_class = AltaIngresoInsumosModelForm
    template_name = "core/alta_insumos.html"
    success_url = reverse_lazy('proovedores')

    def form_valid(self, form):
        response = super().form_valid(form)
        cerveza = self.object.cerveza
        cerveza.stock += self.object.cantidad
        cerveza.save()
        return response

#def contacto(request, nombre):
#    return HttpResponse(f"<h1>Hola {nombre}</h1>")


# Create your views here.
