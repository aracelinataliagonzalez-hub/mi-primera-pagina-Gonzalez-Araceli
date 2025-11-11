from django.shortcuts import render
from inicio.models import Pizza

def inicio(request):
    return render(request, 'inicio.html')

def pedido(request, gusto,tamanio):

    pizza = Pizza(gusto=gusto, tamanio=tamanio)
    pizza.save()
    
    return render(request, 'pedido.html')

# Create your views here.

