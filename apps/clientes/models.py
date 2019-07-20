from django.db import models
from django.core.exceptions  import ValidationError
import os




class Clientes(models.Model):

    def validar_archivo(value):
        ext = os.path.splitext(value.name)[1]
        if ext.lower() == '.jpg':
            pass
        else:
            raise ValidationError('Error')

    nombre = models.CharField(max_length=20, null=True, blank=True)
    apellido = models.CharField(max_length=20, null=True, blank=True)
    numero = models.CharField(max_length=15)
    file = models.FileField(validators=[validar_archivo])

    def __str__(self):
        return str(self.nombre)

    #def save(self, *arg, **kwargs):
    #    self.nombre = Clientes.objects.get(id=1).nombre
    #    super(Clientes, self).save(*arg, **kwargs)



class Clientes_Consolidados(models.Model):
    relacion = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    numero = models.CharField(max_length=15)