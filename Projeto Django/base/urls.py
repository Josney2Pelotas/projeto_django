from django.urls import path
from base.views import *

urlpatterns = [
    path('dados/', ApresentarView.as_view(), name='tela da tabela'),
    path('inserir/', InserirView.as_view(), name='tela de inserção')
]
