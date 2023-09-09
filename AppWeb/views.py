from django.shortcuts import render
from .models import Blog, Mensaje, Imagen, Cisne
from .forms import ImagenForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.contrib.auth.decorators import login_required
from Profile.views import obtenerAvatar#, obtenerImagen
from django.contrib.auth.models import User
from django.db import models

def inicio(request):
    avatar=obtenerAvatar(request)
    return render(request,'AppWeb/inicio.html', {"avatar": avatar})

def aboutme(request):
    return render(request,'AppWeb/aboutMe.html')

def Paisaje(request):
    return render(request,'AppWeb/Paisaje.html')

def Publicitaria(request):
    return render(request,'AppWeb/Publicitaria.html')

def Blancoynegro(request):
    return render(request,'AppWeb/Blancoynegro.html')

#BLOG
class BlogList(ListView):
    model=Blog
    template_name='AppWeb/blogList.html'

class BlogDetail(DetailView):
    model=Blog
    template_name=('AppWeb/blogDetail.html')

class BlogUpdate(UpdateView):
    model=Blog
    template_name='AppWeb/blogUpdate.html'
    success_url=reverse_lazy("blogList")
    fields=['titulo', 'message']

class BlogDelete(DeleteView):
    model=Blog
    success_url=reverse_lazy("blogList")

class BlogCreate2(CreateView):
    model=Blog    
    success_url=reverse_lazy("blogList")
    fields=['titulo', 'message']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(BlogCreate, self).form_valid(form)
    
class BlogCreate(CreateView):
        model=Blog    
        success_url=reverse_lazy("blogList")
        fields=['titulo', 'titulotexto', 'message']

        def form_valid(self, form):
            form.instance.user = self.request.user
            return super(BlogCreate, self).form_valid(form)

#MENSAJE
class MensajeCreate(CreateView):
    model=Mensaje
    success_url=reverse_lazy("blogList")
    fields=['message']
    def form_valid(self, form):
        form.instance.blog_id = self.kwargs['pk']
        form.instance.user = self.request.user
        return super(MensajeCreate, self).form_valid(form)
    
class MensajeList(ListView):
    model=Mensaje
    template_name='AppWeb/mensajeList.html'

class MensajeDetail(DetailView):
    model=Mensaje
    template_name=('AppWeb/mensajeDetail.html')

class MensajeUpdate(UpdateView):
    model=Mensaje
    template_name='AppWeb/mensajeUpdate.html'
    success_url=reverse_lazy("mensajeList")
    fields=['message']

class MensajeDelete(DeleteView):
    model=Mensaje
    success_url=reverse_lazy("mensajeList")

#IMAGEN BLOG

def agregarImagen(request,pk,**kwargs):
    if request.method=="POST":
        form=ImagenForm(request.POST, request.FILES)#request.blog
        if form.is_valid():
            imagen=Imagen(user=request.user, imagen=request.FILES["imagen"], blog=pk)                    
            imagen.save()
            return render(request, "AppWeb/inicio.html", {"imagen":obtenerImagen(request)})
        else:
            return render(request, "AppWeb/agregarImagen.html", {"form": form, "usuario": request.user})
    else:
        form=ImagenForm()
        return render(request, "AppWeb/agregarImagen.html", {"form": form, "usuario": request.user, "imagen":obtenerImagen(request)})
    
def obtenerImagen(request):
    imagenes=Imagen.objects.filter(user=request.user.id)
    if len(imagenes)!=0:        
        return imagenes[0].imagen.url
    else:
        return "no hay imagen"

class ImagenCreate(CreateView):
    model=Imagen
    success_url=reverse_lazy("blogList")
    fields=['imagen']
    def form_valid(self, form):
       form.instance.blog_id = self.kwargs['pk']
       form.instance.user = self.request.user
       form.instance.imagen = self.request.FILES['imagen']
       return super(ImagenCreate, self).form_valid(form)
    
class CisneCreate(CreateView):
    model=Cisne
    success_url=reverse_lazy("CisneList")
    fields=['imagen', 'titulo', 'message']
    def form_valid(self, form):
       form.instance.user = self.request.user
       form.instance.imagen = self.request.FILES['imagen']
       return super(CisneCreate, self).form_valid(form)

class CisneList(ListView):
    model=Cisne
    template_name='AppWeb/cisneList.html'

class CisneDetail(DetailView):
    model=Cisne
    template_name=('AppWeb/CisneDetail.html')

class CisneUpdate(UpdateView):
    model=Cisne
    template_name='AppWeb/CisneUpdate.html'
    success_url=reverse_lazy("cisneList")
    fields=['imagen', 'titulo', 'message']

#class BlogCreate(CreateView):
 #   model=Blog    
  #  success_url=reverse_lazy("blogList")
   # fields=['titulo', 'titulotexto', 'texto']

#    def form_valid(self, form):
    #    form.instance.user = self.request.user
     #   return super(BlogCreate, self).form_valid(form)

#class BlogCreate3(CreateView):
 #       model=Blog    
  #      success_url=reverse_lazy("blogList")
   #     fields=['titulo', 'titulotexto', 'message', 'imagen']

     #   def form_valid(self, form):
      #      form.instance.blog_id = self.kwargs['pk']
       #     form.instance.user = self.request.user
        #    form.instance.imagen = self.request.FILES['imagen']
         #   return super(ImagenCreate, self).form_valid(form)