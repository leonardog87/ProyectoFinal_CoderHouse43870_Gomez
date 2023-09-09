from django import forms
from .models import *

class BlogForm2(forms.Form):
    titulo=forms.CharField(max_length=30)
    message=forms.Textarea()

class BlogForm(forms.Form):
    titulo=forms.CharField(max_length=30)
    titulotexto=forms.CharField(max_length=30)
    message=forms.Textarea()

class MensajeForm(forms.Form):
    message=forms.Textarea()

class ImagenForm(forms.Form):
    imagen=forms.ImageField(label="Imagen")

class CisneForm(forms.Form):
    imagen=forms.ImageField(label="Imagen")
    titulo=forms.CharField(max_length=30)
    message=forms.Textarea()




