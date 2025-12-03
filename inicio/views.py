from django.shortcuts import render, redirect
from inicio.models import Pizza
from inicio.forms import Pedido

def inicio(request):
    return render(request, 'inicio.html')

def pedido(request):
    pizza = None
    if request.method == 'POST':
        formulario = Pedido(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data

            pizza = Pizza(gusto=info.get('gusto'), tamanio=info.get('tamanio'))
            pizza.save()
            return redirect('listado_pizzas')
    else:
        formulario = Pedido()

    return render(request, 'pedido.html', {'formulario':formulario})

def listado_pizzas(request):

    pizzas = Pizza.objects.all() 

    return render(request, 'listado_pizzas.html', {'listado_de_pizzas':pizzas})


# Create your views here.

