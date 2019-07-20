from django import forms
from .models import Clientes

class ClientesForm(forms.ModelForm):
    apellido = forms.CharField(label='apellido', widget=forms.Textarea())
    # label='Apellido', required=False, max_length=20
    class Meta:
        model = Clientes
        fields = '__all__'
    #def __init__(self):
    #    pass
