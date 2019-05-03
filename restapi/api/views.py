# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import UserSerializer
from django.template import loader
import requests

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


def api(request):
    """
    API view that calls weather API, ir retrieves "ciudad" and "apikey" from form
    """
    if not request.user.is_authenticated:
        return HttpResponse('Usuario no autenticado')
    else:
        if 'ciudad' in request.GET:
            location = request.GET['ciudad']
            key = request.GET['apikey']  
            url_weather = "https://api.openweathermap.org/data/2.5/weather?appid="+key+"&q="+location
            url_forecast = "https://api.openweathermap.org/data/2.5/forecast?appid="+key+"&q="+location
            weather = requests.get(url_weather)
            forecast = requests.get(url_forecast)
            message = ("<h1>"+location+"</h1><Br><h1>Clima actual:</Br></h1>"+weather.text+
                        "<Br><h1>Pronóstico:</h1></Br>"+forecast.text)
        else:
            message = 'You submitted an empty form.'
        return HttpResponse(message)
    
def index(request):
    """
    Render index form
    """
    if not request.user.is_authenticated:
        return HttpResponse('Usuario no autenticado')
    else:
        template = loader.get_template("api/index.html")
        return HttpResponse(template.render())
    
