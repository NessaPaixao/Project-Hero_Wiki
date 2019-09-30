from rest_framework import serializers

from herois.models import Heroi
from universos.models import Universo


class UniversoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nome = serializers.CharField()

    def create(self, validated_data):
        universo = Universo.objects.create(**validated_data)
        return universo

    def update(self, instance, validated_data):
        instance.nome = validated_data.get('nome')
        instance.save()
        return instance


