from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from herois.models import Heroi
from herois.serializers import HeroiSerializer


class HeroiViewSet(viewsets.ModelsViewSet):
    filter_backends = [SearchFilter]
    search_fields = ['^nome', '^idade']
    queryset = Heroi.objects.all
    serializer_class = HeroiSerializer


    def index(request):
        herois = Heroi.objects.all()
        contexto = { 'herois': herois}

        return render(request, '.html', contexto)