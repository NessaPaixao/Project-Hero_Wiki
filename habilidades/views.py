from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from habilidades.models import Habilidade
from habilidades.serializers import HabilidadeSerializer


class HabilidadeViewSet(viewsets.ModelsViewSet):
    filter_backends = [SearchFilter]
    search_fields = ['nome']
    queryset = Habilidade.objects.all
    serializer_class = HabilidadeSerializer
