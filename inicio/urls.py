from django.urls import path
from inicio.views import inicio, pedido, listado_pizzas, ver_pedido, ModificarPedido

urlpatterns = [
    path('', inicio, name= 'inicio'),
    path('pedido/', pedido, name= 'pedido'),
    path('ver-pedido/<pizza_id>/', ver_pedido, name= 'ver'),
    path('modificar-pedido/<pk>/', ModificarPedido.as_view(), name= 'modificar'),
    path('listado-pizzas/', listado_pizzas, name= 'listado_pizzas'),
]
