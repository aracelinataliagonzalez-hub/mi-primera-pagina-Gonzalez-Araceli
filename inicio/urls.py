from django.urls import path
from inicio.views import inicio, pedido, listado_pizzas

urlpatterns = [
    path('', inicio, name= 'inicio'),
    path('pedido/', pedido, name= 'pedido'),
    path('listado-pizzas/', listado_pizzas, name= 'listado_pizzas'),
]
