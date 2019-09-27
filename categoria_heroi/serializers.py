from rest_framework import serializers        
from categoria_heroi.models import Categoria


class CategoriaSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nome = serializers.CharField()

    def create(self, validated_data):
        categoria = Categoria.objects.create(**validated_data)
        return categoria

    def update(self, instance, validated_data):
        instance.nome = validated_data.get('nome')
        instance.save()
        return instance