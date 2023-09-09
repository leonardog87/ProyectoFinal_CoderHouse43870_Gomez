from django import forms
from .models import *


class BlogForm(forms.Form):
    imagen=forms.ImageField(label="Imagen")
    titulo=forms.CharField(max_length=30)
    message=forms.Textarea()

class MensajeForm(forms.Form):
    message=forms.Textarea()



