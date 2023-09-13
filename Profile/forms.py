from django import forms
from django.contrib.auth.forms import  UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User

class UserEditForm(UserCreationForm):
    email=forms.EmailField(label="Email")
    password1=None
    password2=None
    first_name=forms.CharField(label='Nombre')
    last_name=forms.CharField(label='Apellido')
    class Meta:
        model=User
        fields=["email", "first_name", "last_name"]
        help_texts = {campo:"" for campo in fields}

class FormularioPasswordEdit(PasswordChangeForm):
    old_password=forms.CharField(label="Contraseña Actual", widget=forms.PasswordInput)
    new_password1=forms.CharField(label="Nueva contraseña", widget=forms.PasswordInput)   
    new_password2=forms.CharField(label="Repita la contraseña", widget=forms.PasswordInput)    
    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')

class PasswordEditForm(UserCreationForm):
    email=None
    password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)
    first_name=None
    last_name=None    
    class Meta:
        model=User
        fields=["password1", "password2"]
        help_texts = {campo:"" for campo in fields}

