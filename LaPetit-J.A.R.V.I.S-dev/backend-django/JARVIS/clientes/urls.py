from django.urls import path
from .views import clientes_list, cliente_detail

urlpatterns = [
    path('clientes/', clientes_list, name='clientes_list'),
    path('clientes/<int:id>/', cliente_detail, name='cliente_detail'),
]