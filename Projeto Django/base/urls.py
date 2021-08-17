from django.urls import path
from base.views import *

urlpatterns = [
    path('dados/', GetView.as_view(), name='tela da tabela'),
    path('inserir/', InsertView.as_view(), name='tela de inserção'),
    path('update/', UpdateView.as_view(), name='tela de update'),
    path('update/', DeleteView.as_view(), name='tela de delecao')
]
