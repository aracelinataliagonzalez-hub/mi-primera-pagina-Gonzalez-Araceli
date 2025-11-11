from django.db import models

class Pizza(models.Model):
    gusto = models.CharField(max_length=30)
    tamanio = models.CharField(max_length=30)

    
# Create your models here.
