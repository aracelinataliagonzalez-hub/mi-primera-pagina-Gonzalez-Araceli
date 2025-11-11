from django.urls import path
from inicio.views import inicio, pedido, listado_pizzas

urlpatterns = [
    path('', inicio),
    path('pedido/<gusto>/<tamanio>', pedido),
    path('listado-pizzas/', listado_pizzas),
]
