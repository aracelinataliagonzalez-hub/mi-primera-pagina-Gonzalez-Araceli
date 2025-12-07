from django.db import models

class Pizza(models.Model):
    gusto = models.CharField(max_length=30)
    tamanio = models.CharField(max_length=30)
    imagen = models.ImageField(upload_to='imagenes_pizzas', null=True)

    def __str__(self):
        return f' Pizza({self.id}): {self.gusto} - {self.tamanio}'


    
# Create your models here.
