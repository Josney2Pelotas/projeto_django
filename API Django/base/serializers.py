from rest_framework import serializers
from base.models import *


class GetSerializer(serializers.Serializer):
    dados = serializers.ListField()
    ids = serializers.ListField()
    user = serializers.CharField()


class InsertIdsSerializer(serializers.Serializer):
    ids = serializers.ListField()


class InsertSerializer(serializers.Serializer):
    valor = serializers.IntegerField()
    tabela1_id = serializers.IntegerField()

    def create(self, validated_data):
        return Tabela2.objects.create(**validated_data)


class UpdateSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    coluna2 = serializers.CharField()
    coluna1 = serializers.IntegerField()

    def update(self, instance, validated_data):
        instance.coluna1 = validated_data.get('coluna1', instance.coluna1)
        instance.coluna2 = validated_data.get('coluna2', instance.coluna2)
        instance.save()
        return instance
