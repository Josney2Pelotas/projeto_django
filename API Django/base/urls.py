from django.urls import path
from base.views import *

urlpatterns = [
    path('get_infos/', APIView.as_view(), name='classe de teste')
]