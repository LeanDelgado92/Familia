from django.shortcuts import render
from familia.models import Familiar

def index(request):
    return render(request, "Familia/saludar.html")

def mostrar_familiares(request):
    lista_familiares = Familiar.objects.all()
    return render(request, "Familia/familiares.html", {"lista_familiares": lista_familiares})
