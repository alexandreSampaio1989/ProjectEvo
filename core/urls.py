from django.urls import path
from core.views import index, contact, product

urlpatterns = [
    path('', index),
    path('contato', contact, name='contato'),
    path('produto/<int:pk>', product, name='produto')
]