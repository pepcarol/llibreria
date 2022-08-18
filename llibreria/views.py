from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def inici(request):
    return render(request, 'pagines/inici.html')
def nosaltres(request):
    return render(request, 'pagines/nosaltres.html')

# Pagines accions

def llibres(request):
    return render(request, 'llibres/index.html')
def crear_llibre(request):
    return render(request, 'llibres/crear.html')

def editar_llibre(request):
    return render(request, 'llibres/editar.html')
