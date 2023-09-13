from django import forms
from .models import *


class BlogForm(forms.Form):
    imagen=forms.ImageField(label="Imagen")
    titulofoto=forms.CharField(max_length=30)
    titulomessage=models.CharField(max_length=30)
    message=forms.Textarea()

class MensajeForm(forms.Form):
    message=forms.Textarea()



