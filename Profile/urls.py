from django.urls import path
from .views import *

urlpatterns = [
    path('editarPerfil/', editarPerfil, name='editarPerfil'),
    path('PasswordEdit/', PasswordEdit.as_view(), name='PasswordEdit'),
    path('agregarAvatar/', agregarAvatar, name='agregarAvatar'),
    path('editarPassword/', editarPassword, name='editarPassword'),
    #path('agregarImagen/', agregarImagen, name='agregarImagen'),
]
