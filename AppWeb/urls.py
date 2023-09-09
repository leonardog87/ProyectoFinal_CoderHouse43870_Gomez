from django.urls import path
from .views import *

urlpatterns = [

# BLOG
    path('blogForm/nuevo/', BlogCreate.as_view(), name="blogForm"),
    path('blogList/', BlogList.as_view(), name="blogList"),
    path('blogDetail/<pk>', BlogDetail.as_view(), name="blogDetail"),
    path('blogUpdate/<pk>', BlogUpdate.as_view(), name="blogUpdate"),
    path('blogList/delete/<pk>', BlogDelete.as_view(), name="blogDelete"),

# MENSAJE
    path('mensajeForm/nuevo/', MensajeCreate.as_view(), name="mensajeForm"),
    path('mensajeList/', MensajeList.as_view(), name="mensajeList"),
    path('mensajeDetail/<pk>', MensajeDetail.as_view(), name="mensajeDetail"),
    path('mensajeUpdate/<pk>', MensajeUpdate.as_view(), name="mensajeUpdate"),
    path('mensajeList/delete/<pk>', MensajeDelete.as_view(), name="mensajeDelete"), 

#BLOG MENSAJE
    path('blogDetail/<pk>/mensaje/', MensajeCreate.as_view(), name="mensaje"),
   # path('agregarImagen/', agregarImagen, name='agregarImagen'),
    path('blogDetail/<pk>/imagen', ImagenCreate.as_view(), name='ImagenCreate'),

#ABOUT ME
    path('aboutMe/', aboutme, name="aboutme"),

#TIPOS DE FOTOGRAFIA
    path('Paisaje/', Paisaje, name="Paisaje"),
    path('Publicitaria/', Publicitaria, name="Publicitaria"),
    path('Blancoynegro/', Blancoynegro, name="Blancoynegro"),

#PROBANDO
    path('CisneForm/nuevo/', CisneCreate.as_view(), name='CisneCreate'),
    path('CisneList', CisneList.as_view(), name='CisneList'),
    path('CisneDetail/<pk>', CisneDetail.as_view(), name="CisneDetail"),
    path('CisneUpdate/<pk>', CisneUpdate.as_view(), name="CisneUpdate"),
]
