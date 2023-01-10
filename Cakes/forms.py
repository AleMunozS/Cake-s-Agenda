from . import models
from django import forms
from bootstrap_datepicker_plus.widgets import DatePickerInput

class Form(forms.ModelForm):
    
    class Meta():
        model = models.Pedidos
        fields = ('sabor', 'persona','fecha_entrega', 'direccion', 'direccion_URL', 'detalles',)

        widgets = {
            'fecha_entrega': DatePickerInput()
        } 
    