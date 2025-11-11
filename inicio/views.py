from django.shortcuts import render
from inicio.models import Pizza

def inicio(request):
    return render(request, 'inicio.html')

def pedido(request, gusto,tamanio):

    pizza = Pizza(gusto=gusto, tamanio=tamanio)
    pizza.save()

    return render(request, 'pedido.html',{'objeto_guardado':pizza})

def listado_pizzas(request):

    pizzas = Pizza.objects.all() 

    return render(request, 'listado_pizzas.html', {'listado_de_pizzas':pizzas})


# Create your views here.

