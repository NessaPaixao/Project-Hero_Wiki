from rest_framework import serializers

from categoria_heroi.models import Categoria
from habilidades.models import Habilidade
from herois.models import Heroi
from universos.models import Universo


class UniversoDTOSerializer(serializers.Serializers):
    id = serializers.IntegerField()
    nome = serializers.CharField(read_only=True)


class HabilidadeDTOSerializer(serializers.Serializers):
    id = serializers.IntegerField()
    nome = serializers.CharField(read_only=True)


class CategoriaDTOSerializer(serializers.Serializers):
    id = serializers.IntegerField()
    nome = serializers.CharField(read_only=True)


class HeroiSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    nome = serializers.CharField(read_only=True)
    idade = serializers.IntegerField()
    habilidade = HabilidadeDTOSerializer(many=True)
    categoria = CategoriaDTOSerializer()
    universo = UniversoDTOSerializer()

    def create(self, validated_data):
        universo_data = validated_data.pop('universo')
        universo = Universo.objects.get(id=universo_data['id'])
        categoria_data = validated_data.pop('categoria')
        categoria = Categoria.objects.get(id=categoria_data['id'])
        habilidade_data = validated_data.pop('habilidade')
        lista = []
        for habilidade in habilidade_data:
            lista.insert(Habilidade.objects.get(id=habilidade['id']))
        heroi = Heroi.objects.create(universo=universo, categoria=categoria, habilidade=lista, **validated_data)
        return heroi

    def update(self, instance, validated_data):
        instance.nome = validated_data.get('nome')
        instance.idade = validated_data.get('idade')
        instance.universo = validated_data.get('universo')
        instance.categoria = validated_data.get('categoria')
        instance.lista = validated_data.get('habilidade')
        instance.save()
        return instance