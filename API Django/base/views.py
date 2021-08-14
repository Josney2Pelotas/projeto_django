from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from base.serializers import *
from base.querys import *


class TabelaView(APIView):
    def get(self, request):
        dados_serializer = {'dados': queryvalores(request.data), 'ids': query_id()}
        serializer = TabelaSerializer(dados_serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)


class InsertView(APIView):
    def get(self, request):
        dados_serializer = {'ids': query_id()}
        serializer = InsertIdsSerializer(dados_serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = InsertSerializer(data=request.POST.dict())
        if serializer.is_valid():
            serializer.create(serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
