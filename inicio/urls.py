from django.urls import path
from inicio.views import inicio, pedido

urlpatterns = [
    path('', inicio),
    path('pedido/<gusto>/<tamanio>', pedido),
]
