from django.db import models
from django.utils import timezone
from django.urls import reverse
import datetime
# Create your models here.

class Pedidos(models.Model):
    sabor_Choices = (('Chocolate', 'chocolate'),
                     ('Vainilla', 'vainilla'),
                     ('Confetti', 'confetti'),
                     )
    sabor = models.CharField(max_length=208,choices=sabor_Choices)
    persona = models.CharField(max_length=208)
    fecha_pedido = models.DateField(default=timezone.now)
    fecha_entrega = models.DateField(blank=False, null=False)
    direccion = models.CharField(max_length=200)
    direccion_URL = models.URLField(blank=True, null=True)
    detalles = models.TextField(blank=True, null=True)
    entre = models.BooleanField(default=False)
    
    def __str__(self):
        return self.persona

    def get_absolute_url(self):
        return reverse("Cakes:pedidos_list")
    
    def entregado(self):
       self.entregado = True

    def days(self):
        diff = abs((datetime.date.today()-self.fecha_entrega).days)
        if diff<=1:
            return 'table-danger'
        if diff==2:
            return 'table-warning'
        if diff>=3 and diff <= 5:
            return 'table-info'
            



## SI mi direccion de pedido ya paso hace 5 dias borrar de Entregados

