from django.contrib import admin
from .models import Clientes, Clientes_Consolidados
from .forms import ClientesForm


class Clientes_Consolidados_Admin(admin.TabularInline):
    model = Clientes_Consolidados
    extra = 0
    verbose_name = 'Clientesss COnsolidados'




class Clientes_Admin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'numero')
    inlines = [Clientes_Consolidados_Admin]

    form = ClientesForm

    def save_model(self, request, obj, form, change):
        Clientes.objects.create(nombre=obj.nombre, apellido='Taxykistan', numero='232344')
        super(Clientes_Admin, self).save_model(request, obj, form, change)

admin.site.register(Clientes, Clientes_Admin)

