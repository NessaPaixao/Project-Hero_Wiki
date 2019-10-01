from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from universos.models import Universo
from universos.serializers import UniversoSerializer


class UniversoViewSet(viewsets.ModelsViewSet):
    filter_backends = [SearchFilter]
    search_fields = ['nome']
    queryset = Universo.objects.all
    serializer_class = UniversoSerializer







































# Create your views here.
