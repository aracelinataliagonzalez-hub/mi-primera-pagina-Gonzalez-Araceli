from django import forms 

class Pedido(forms.Form):
    gusto = forms.CharField(max_length=30)
    tamanio = forms.CharField(max_length=30)
    imagen = forms.ImageField(required=False)

class BuscarPizza(forms.Form):
    gusto = forms.CharField(max_length=30, required=False)
