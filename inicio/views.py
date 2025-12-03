from django.shortcuts import render, redirect
from inicio.models import Pizza
from inicio.forms import Pedido
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

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

def ver_pedido(request, pizza_id):
    pizza = Pizza.objects.get(id = pizza_id)
    
    return render(request, 'ver_pedido.html', {'pizza': pizza})


class ModificarPedido(UpdateView):
    model = Pizza
    template_name = 'modificar_pedido.html'
    fields = '__all__'
    success_url = reverse_lazy('listado_pizzas')
    

# Create your views here.

