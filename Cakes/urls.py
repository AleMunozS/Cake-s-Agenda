from django.urls import path, re_path
from . import views


app_name = 'Cakes'
urlpatterns = [
    path('', views.PedidoListView.as_view(), name='pedidos_list'),
    path("create/", views.PedidoCreateView.as_view(), name="pedidos_new"),
    re_path(r'^pedido/(?P<pk>\d+)/delete/$', views.PedidoDeleteView.as_view(), name='pedidos_delete'),
    re_path(r'^pedido/(?P<pk>\d+)/update/$', views.PedidoUpdateView.as_view(), name='pedidos_update'),
    re_path(r'^pedido/(?P<pk>\d+)/detail/$', views.PedidoDetailView.as_view(), name='pedidos_detail'),
]
