from django.shortcuts import render

def inicio(request):
    return render(request, inicio.html)

def pedido(request):
    return render(request, pedido.html)

# Create your views here.
