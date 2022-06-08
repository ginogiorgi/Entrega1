from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class SeriePelicula(models.Model):
    nombre = models.CharField(max_length=50)
    categoria = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=200)
    origen = models.CharField(max_length=30)
    cant_capitulos = models.IntegerField()
    genero = models.CharField(max_length=30)
    puntuacion = models.IntegerField()
    
    def __str__(self) -> str:
        return f"nombre: {self.nombre} - categoria: {self.categoria} - genero: {self.genero}"
    
class MangaComic(models.Model):
    nombre = models.CharField(max_length=50)
    categoria = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=200)
    origen = models.CharField(max_length=30)
    cant_tomos = models.IntegerField()
    genero = models.CharField(max_length=30)
    puntuacion = models.IntegerField()
    
    def __str__(self) -> str:
        return f"nombre: {self.nombre} - categoria: {self.categoria} - genero: {self.genero}"

class Profile(models.Model):
    nombre_usuario = models.CharField(max_length=30)
    dni = models.IntegerField(0)
    email = models.EmailField()
    fecha_nacimiento = models.DateField()
    
    def __str__(self) -> str:
        return f"Nombre: {self.nombre_usuario} - categoria: {self.dni} - genero: {self.email}"   
    
class Post(models.Model):
    timestamp = models.DateField(default=timezone.now)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post')
    
    class Meta:
        ordering = ['-timestamp']
        
    def __str__(self) -> str:
        return self.content
    

