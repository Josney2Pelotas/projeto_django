from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from base.serializers import *
from base.querys import *


class APIView(ListAPIView):
    def get(self, request):
        dados_serializer = {'dados': QueryTeste(request.data)}
        serializer = TabelaSerializer(dados_serializer)
        return Response(serializer.data)
