from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from .forms import ContactoForm, AltaCervezaModelForm
from .models import Cerveza

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

@login_required(login_url='/proovedores/login')
def proovedores(request):
    
    return render(request, "core/proovedores.html")

class ProovedoresView(LoginRequiredMixin):
    pass

#def contacto(request, nombre):
#    return HttpResponse(f"<h1>Hola {nombre}</h1>")


# Create your views here.
