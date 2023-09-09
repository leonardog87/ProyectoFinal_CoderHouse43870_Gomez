from django.db import models
from django.contrib.auth.models import User

class Avatar(models.Model):
    imagen=models.ImageField(upload_to="avatars")
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

#class Imagen(models.Model):
 #   imagen=models.ImageField(upload_to="blog")
  #  user=models.ForeignKey(User, related_name='imagenes', on_delete=models.CASCADE, null=True, blank=True)