from django.shortcuts import render
from .forms import UserEditForm, FormularioPasswordEdit, AvatarForm, PasswordEditForm#, ImagenForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin  
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from .models import Avatar#, Imagen


def obtenerAvatar(request):
    avatares=Avatar.objects.filter(user=request.user.id)
    if len(avatares)!=0:        
        return avatares[0].imagen.url
    else:
        return "/media/avatars/avatarpordefecto.png"
    
def editarPerfil(request):
    avatar=obtenerAvatar(request)
    usuario=request.user
    if request.method=="POST":
        form=UserEditForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usuario.first_name=info["first_name"]
            usuario.last_name=info["last_name"]
            usuario.email=info["email"]
            usuario.save()
            return render(request, "AppWeb/inicio.html",{"avatar": avatar})
        else:
            return render(request, "Profile/editarPerfil.html", {"form": form, "nombreusuario":usuario.username, "avatar": avatar})
    else:
        form=UserEditForm(instance=usuario)
        return render(request, "Profile/editarPerfil.html", {"form": form, "nombreusuario":usuario.username, "avatar": avatar})

class PasswordEdit(PasswordChangeView):
    form_class = FormularioPasswordEdit
    template_name = 'Profile/PasswordEdit.html'
    success_url = reverse_lazy('inicio')
    
def agregarAvatar(request):
    if request.method=="POST":
        form=AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            avatar=Avatar(user=request.user, imagen=request.FILES["imagen"])            
            avatarViejo=Avatar.objects.filter(user=request.user)
            if len(avatarViejo)>0:
                avatarViejo[0].delete()
            avatar.save()
            return render(request, "AppWeb/inicio.html", {"avatar":obtenerAvatar(request)})
        else:
            return render(request, "Profile/agregarAvatar.html", {"form": form, "usuario": request.user})
    else:
        form=AvatarForm()
        return render(request, "Profile/agregarAvatar.html", {"form": form, "usuario": request.user, "avatar":obtenerAvatar(request)})
    
def editarPassword(request):
    avatar=obtenerAvatar(request)
    usuario=request.user
    if request.method=="POST":
        form=PasswordEditForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usuario.password1=info["password1"]
            usuario.password2=info["password2"]
            usuario.save()
            return render(request, "Profile/passwordExitoso.html",{"avatar": avatar})
        else:
            return render(request, "Profile/editarPassword.html", {"form": form, "nombreusuario":usuario.username, "avatar": avatar})
    else:
        form=PasswordEditForm(instance=usuario)
        return render(request, "Profile/editarPassword.html", {"form": form, "nombreusuario":usuario.username, "avatar": avatar})
    
#IMAGEN BLOG

#def agregarImagen(request):
    if request.method=="POST":
        form=ImagenForm(request.POST, request.FILES)
        if form.is_valid():
            imagen=Imagen(user=request.user, imagen=request.FILES["imagen"])                    
            imagen.save()
            return render(request, "AppWeb/inicio.html", {"imagen":obtenerImagen(request)})
        else:
            return render(request, "Profile/agregarImagen.html", {"form": form, "usuario": request.user})
    else:
        form=ImagenForm()
        return render(request, "Profile/agregarImagen.html", {"form": form, "usuario": request.user, "imagen":obtenerImagen(request)})
    
#def obtenerImagen(request):
    imagenes=Imagen.objects.filter(user=request.user.id)
    if len(imagenes)!=0:        
        return imagenes[0].imagen.url
    else:
        return "no hay imagen"