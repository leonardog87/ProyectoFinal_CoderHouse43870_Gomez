from django.db import models
from django.contrib.auth.models import User
from Profile.models import Avatar


# Create your models here.

class Blog2(models.Model):    
    titulo=models.CharField(max_length=30)
    message=models.TextField(null=True, blank=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=False)
    def __str__(self):
        return f"{self.titulo} - {self.message} - {self.user}"

class Blog(models.Model):    
    titulo=models.CharField(max_length=30)
    titulotexto=models.CharField(max_length=30)
    message=models.TextField(null=True, blank=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=False)
    def __str__(self):
        return f"{self.titulo} - {self.titulotexto} - {self.message} - {self.user}"
    
class Mensaje(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=False)
    blog=models.ForeignKey(Blog, related_name='mensajes', on_delete=models.CASCADE, null=True)
    message=models.TextField(null=True, blank=True)    
    def __str__(self):
        return f"{self.message} - {self.blog}"
    

class Imagen(models.Model):
    imagen=models.ImageField(upload_to="blog")
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    blog=models.ForeignKey(Blog, related_name='images', on_delete=models.CASCADE, null=True, blank=True)


class Cisne(models.Model):
    imagen=models.ImageField(upload_to="blog")
    titulo=models.CharField(max_length=30)
    message=models.TextField(null=True, blank=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)




    


 