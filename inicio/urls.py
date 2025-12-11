from django.urls import path
from inicio.views import inicio, crear_pizza, listado_pizzas, ver_pizza, ModificarPizza, EliminarPizza, acerca_de_mi

urlpatterns = [
    path('', inicio, name= 'inicio'),
    path('crear_pizza/', crear_pizza, name= 'crear_pizza'),
    path('ver-pizza/<pizza_id>/', ver_pizza, name= 'ver'),
    path('modificar-pizza/<pk>/', ModificarPizza.as_view(), name= 'modificar'),
    path('eliminar-pizza/<pk>/', EliminarPizza.as_view(), name= 'eliminar'),
    path('listado-pizzas/', listado_pizzas, name= 'listado_pizzas'),
    path('acerca-de-mi/', acerca_de_mi, name= 'acerca_de_mi'),
]
