from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from categoria_heroi.models import Categoria
from categoria_heroi.serializers import CategoriaSerializer


class CategoriaViewSet(viewsets.ModelsViewSet):
    filter_backends = [SearchFilter]
    search_fields = ['nome']
    queryset = Categoria.objects.all
    serializer_class = CategoriaSerializer