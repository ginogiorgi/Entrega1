from django import forms

class SeriePeliculaFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    categoria = forms.CharField(max_length=30)
    descripcion = forms.CharField(max_length=200)
    origen = forms.CharField(max_length=30)
    cant_capitulos = forms.IntegerField()
    genero = forms.CharField(max_length=30)
    puntuacion = forms.IntegerField()
    
class MangaComicFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    categoria = forms.CharField(max_length=30)
    descripcion = forms.CharField(max_length=200)
    origen = forms.CharField(max_length=30)
    cant_tomos = forms.IntegerField()
    genero = forms.CharField(max_length=30)
    puntuacion = forms.IntegerField()
    
class ProfileFormulario(forms.Form):
    nombre_usuario = forms.CharField(max_length=30)
    dni = forms.IntegerField()
    email = forms.EmailField()
    fecha_nacimiento = forms.DateField()
    
    