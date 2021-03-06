from django.urls import path
from base.views import *

urlpatterns = [
    path('get_infos/', GetView.as_view(), name='classe da busca'),
    path('insert_infos/', InsertView.as_view(), name='classe de insercao'),
    path('update_infos/', UpdateView.as_view(), name='classe de update'),
    path('delete_infos/', UpdateView.as_view(), name='classe de delecao')
]
