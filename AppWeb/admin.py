from django.contrib import admin

# Register your models here.

from .models import Blog, Mensaje

admin.site.register(Blog)
admin.site.register(Mensaje)