from django.shortcuts import render
from django.views.generic import DetailView, DeleteView, CreateView, ListView, UpdateView
from . import forms
from . import models
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from bootstrap_datepicker_plus.widgets import DateTimePickerInput
# Create your views here.

class PedidoCreateView(CreateView):
    form_class = forms.Form
    model = models.Pedidos
    

class PedidoUpdateView(UpdateView):
    form_class = forms.Form
    model = models.Pedidos

class PedidoDeleteView(DeleteView):
    model=models.Pedidos
    success_url = reverse_lazy('Cakes:pedidos_list')

class PedidoDetailView(DetailView):
    model = models.Pedidos

class PedidoListView(ListView):
    model = models.Pedidos
    
    def get_queryset(self):
        return models.Pedidos.objects.filter(entre=False).order_by('fecha_entrega')

class EntregadosListView(ListView):
    model = models.Pedidos

    def get_queryset(self):
        return models.Pedidos.objects.filter(entre=True).order_by('-fecha_entrega')

        
    
