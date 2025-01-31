from django.urls import path
from core.views import index, contato, produto, form_produto

urlpatterns = [
    path('', index, name='index'),
    path('contato', contato, name='contato'),
    path('produto/<int:pk>', produto, name='produto'),
    path('produto/novo', form_produto, name='form_produto'),
]