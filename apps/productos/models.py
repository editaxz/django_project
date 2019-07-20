from django.db import models
from clientes.models import Clientes
#from Clientes.models import Clientes


class Productos(models.Model):
    nombre = models.CharField(max_length=20)
    precio = models.DecimalField(max_digits=10, decimal_places=10, verbose_name=u'Precio')
    relacion = models.ForeignKey(Clientes, on_delete=models.CASCADE)



    def __str__(self):
        return str(self.nombre)