from django.shortcuts import render, redirect
from inicio.models import Pizza
from inicio.forms import Pedido, BuscarPizza
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

def inicio(request):
    return render(request, 'inicio.html')

@login_required
def pedido(request):
    pizza = None
    if request.method == 'POST':
        formulario = Pedido(request.POST, request.FILES)
        if formulario.is_valid():
            info = formulario.cleaned_data

            pizza = Pizza(gusto=info.get('gusto'), tamanio=info.get('tamanio'), imagen=info.get('imagen'))
            pizza.save()
            return redirect('listado_pizzas')
    else:
        formulario = Pedido()

    return render(request, 'pedido.html', {'formulario':formulario})

def listado_pizzas(request):
    formulario = BuscarPizza(request.GET)
    if formulario.is_valid():
        gusto_buscado = formulario.cleaned_data.get('gusto')
        listado_pizza = Pizza.objects.filter(gusto__icontains = gusto_buscado)

    return render(request, 'listado_pizzas.html', {'listado_de_pizzas':listado_pizza, 'formulario':formulario})

def ver_pedido(request, pizza_id):
    pizza = Pizza.objects.get(id = pizza_id)
    
    return render(request, 'ver_pedido.html', {'pizza': pizza})


class ModificarPedido(LoginRequiredMixin, UpdateView):
    model = Pizza
    template_name = 'modificar_pedido.html'
    fields = '__all__'
    success_url = reverse_lazy('listado_pizzas')
    
class EliminarPedido(LoginRequiredMixin, DeleteView):
    model = Pizza
    template_name = 'eliminar_pedido.html'
    success_url = reverse_lazy('listado_pizzas')
    
# Create your views here.

