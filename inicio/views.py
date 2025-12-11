from django.shortcuts import render, redirect
from inicio.models import Pizza
from inicio.forms import PizzaFormulario, BuscarPizza
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

def inicio(request):
    return render(request, 'inicio.html')

@login_required
def crear_pizza(request):
    pizza = None
    if request.method == 'POST':
        formulario = PizzaFormulario(request.POST, request.FILES)
        if formulario.is_valid():
            info = formulario.cleaned_data

            pizza = Pizza(gusto=info.get('gusto'), tamanio=info.get('tamanio'), precio =info.get('precio'), imagen=info.get('imagen'))
            pizza.save()
            return redirect('listado_pizzas')
    else:
        formulario = PizzaFormulario()

    return render(request, 'crear_pizza.html', {'formulario':formulario})

def listado_pizzas(request):
    formulario = BuscarPizza(request.GET)
    if formulario.is_valid():
        gusto_buscado = formulario.cleaned_data.get('gusto')
        listado_pizza = Pizza.objects.filter(gusto__icontains = gusto_buscado)

    return render(request, 'listado_pizzas.html', {'listado_de_pizzas':listado_pizza, 'formulario':formulario})

def ver_pizza(request, pizza_id):
    pizza = Pizza.objects.get(id = pizza_id)
    
    return render(request, 'ver_pizza.html', {'pizza': pizza})


class ModificarPizza(LoginRequiredMixin, UpdateView):
    model = Pizza
    template_name = 'modificar_pizza.html'
    fields = '__all__'
    success_url = reverse_lazy('listado_pizzas')
    
class EliminarPizza(LoginRequiredMixin, DeleteView):
    model = Pizza
    template_name = 'eliminar_pizza.html'
    success_url = reverse_lazy('listado_pizzas')

def acerca_de_mi(resquest):
    return render(resquest, 'acerca_de_mi.html')    
    
# Create your views here.

