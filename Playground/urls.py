from django.contrib import admin
from django.urls import path, include 
from Playground.views import inicio, seriesPeliculas, mangaComic, login

urlpatterns = [
    path('', inicio, name = 'Inicio'),
    path('seriesypeliculas/', seriesPeliculas, name = 'SeriesPeliculas' ),
    path('mangaycomic/', mangaComic, name = "MangasComics"),
    path('login/', login, name = 'Login' ),
]
