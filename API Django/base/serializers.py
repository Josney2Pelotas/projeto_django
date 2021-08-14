from rest_framework import serializers


class TabelaSerializer(serializers.Serializer):
    dados = serializers.ListField()
