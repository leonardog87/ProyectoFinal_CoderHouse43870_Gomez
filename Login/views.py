from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from AppWeb.views import inicio
from Profile.views import obtenerAvatar

def login_request(request):
    avatar=obtenerAvatar(request)
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            info=form.cleaned_data
            user=info["username"]
            clave=info["password"]
            usuario=authenticate(username=user, password=clave)
            if usuario is not None:
                login(request, usuario)
                return render(request, "AppWeb/inicio.html", {"avatar": avatar})
            else:
                return render(request,"AppWeb/inicio.html", {"form":form, "avatar": avatar})
        else:
            return render(request,"Login/login.html", {"form":form})
    else:
        form=AuthenticationForm()
        return render(request,"Login/login.html", {"form":form, "avatar": avatar})