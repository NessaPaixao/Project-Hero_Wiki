from rest_framework import serializers
from habilidades.models import Habilidade


class HabilidadeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nome = serializers.CharField()

    def create(self, validated_data):
        habilidade = Habilidade.objects.create(**validated_data)
        return habilidade

    def update(self, instance, validated_data):
        instance.nome = validated_data.get('nome')
        instance.save()
        return instance