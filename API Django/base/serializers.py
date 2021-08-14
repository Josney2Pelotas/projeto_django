from rest_framework import serializers
from base.models import *


class TabelaSerializer(serializers.Serializer):
    dados = serializers.ListField()
    ids = serializers.ListField()


class InsertIdsSerializer(serializers.Serializer):
    ids = serializers.ListField()


class InsertSerializer(serializers.Serializer):
    valor = serializers.IntegerField()
    tabela1_id = serializers.IntegerField()

    def create(self, validated_data):
        return Tabela2.objects.create(**validated_data)
