from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def index(request):
    return render(request, "index.html")

def contacto(request, nombre):
    return HttpResponse(f"<h1>Hola {nombre}</h1>")


# Create your views here.
