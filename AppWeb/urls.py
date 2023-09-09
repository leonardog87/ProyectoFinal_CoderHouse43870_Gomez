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
    path('mensajeForm/nuevo/', MensajeCreate.as_view(), name="mensaje"),
    path('blogDetail/<pk>/mensaje/', MensajeCreate.as_view(), name="bmensaje"),

#ABOUT ME
    path('aboutMe/', aboutme, name="aboutme"),

#TIPOS DE FOTOGRAFIA
    path('Paisaje/', Paisaje, name="Paisaje"),
    path('Publicitaria/', Publicitaria, name="Publicitaria"),
    path('Blancoynegro/', Blancoynegro, name="Blancoynegro"),

]
