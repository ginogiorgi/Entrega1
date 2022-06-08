from turtle import pu
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from Playground.forms import SeriePeliculaFormulario, MangaComicFormulario, ProfileFormulario
from Playground.models import *

def inicio(request):
    plantilla = loader.get_template('inicio.html')
    documento = plantilla.render()
    return HttpResponse(documento)

def seriesPeliculas(request):
    if request.method == "POST":
        
        miFormulario = SeriePeliculaFormulario(request.POST)
            
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            
        nombre = info['nombre']    
        categoria = info['categoria']
        descripcion = info ['descripcion']
        origen = info ['origen']
        cant_cap = info ['cant_capitulos']
        genero = info ['genero']
        puntuacion = info ['puntuacion']
        anime = SeriePelicula(nombre = nombre, categoria = categoria, descripcion = descripcion, origen = origen, cant_capitulos = cant_cap, genero = genero, puntuacion = puntuacion)
        anime.save()
        
        return render(request, 'inicio.html')
    
    else:
        miFormulario = SeriePeliculaFormulario()
    
    if request.GET:
        
        nombre = request.GET['nombre']
        objetos = SeriePelicula.objects.filter(nombre__icontains = nombre)
        return render(request, 'busquedaseriepelicula.html', {'objetos': objetos, 'nombre':nombre})
        
    return render(request, 'seriesypeliculas.html',{"formulario":miFormulario})

def mangaComic(request):
    if request.method == "POST":
        
        miFormulario = MangaComicFormulario(request.POST)
            
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            
        nombre = info['nombre']    
        categoria = info['categoria']
        descripcion = info ['descripcion']
        origen = info ['origen']
        cant_tomo = info ['cant_tomos']
        genero = info ['genero']
        puntuacion = info ['puntuacion']
        anime = MangaComic(nombre = nombre, categoria = categoria, descripcion = descripcion, origen = origen, cant_tomos = cant_tomo, genero = genero, puntuacion = puntuacion)
        anime.save()
        
        return render(request, 'inicio.html')
    
    else:

        miFormulario = MangaComicFormulario()
        
    return render(request, 'mangaycomic.html',{"formulario":miFormulario})

def login(request):
    if request.method == "POST":
        
        miFormulario = ProfileFormulario(request.POST)
        
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            
        nombre = info['nombre_usuario']
        dni = info['dni']
        email = info['email']
        fecha = info['fecha_nacimiento']
        
        usuario = Profile(nombre_usuario = nombre, dni = dni, email = email, fecha_nacimiento = fecha )
        usuario.save()
        return render(request, 'inicio.html')
    
    else:

        miFormulario = ProfileFormulario()
        
    return render(request, 'login.html',{"formulario":miFormulario})
        