from django.urls import path
from base.views import *

urlpatterns = [
    path('dados/', TesteView.as_view(), name='tela de teste')
]
