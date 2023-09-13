from django.shortcuts import render
from .forms import UserEditForm, FormularioPasswordEdit, PasswordEditForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin  
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView

def editarPerfil(request):
    usuario=request.user
    if request.method=="POST":
        form=UserEditForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usuario.first_name=info["first_name"]
            usuario.last_name=info["last_name"]
            usuario.email=info["email"]
            usuario.save()
            return render(request, "AppWeb/inicio.html")
        else:
            return render(request, "Profile/editarPerfil.html", {"form": form, "nombreusuario":usuario.username})
    else:
        form=UserEditForm(instance=usuario)
        return render(request, "Profile/editarPerfil.html", {"form": form, "nombreusuario":usuario.username})

class PasswordEdit(PasswordChangeView):
    form_class = FormularioPasswordEdit
    template_name = 'Profile/PasswordEdit.html'
    success_url = reverse_lazy('inicio')
    
def editarPassword(request):
    usuario=request.user
    if request.method=="POST":
        form=PasswordEditForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usuario.password1=info["password1"]
            usuario.password2=info["password2"]
            usuario.save()
            return render(request, "AppWeb/inicio.html")
        else:
            return render(request, "Profile/editarPassword.html", {"form": form, "nombreusuario":usuario.username})
    else:
        form=PasswordEditForm(instance=usuario)
        return render(request, "Profile/editarPassword.html", {"form": form, "nombreusuario":usuario.username})
    
