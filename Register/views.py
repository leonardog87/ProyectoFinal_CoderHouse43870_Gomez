from django.shortcuts import render
from .forms import RegisterUserForm
from AppWeb.views import inicio


def register(request):
    if request.method=="POST":
        form=RegisterUserForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre_usuario=info["username"]
            form.save()
            return render(request, "AppWeb/inicio.html")
        else:
            return render(request,"Register/register.html", {"form":form})
    else:
        form=RegisterUserForm()
        return render(request,"Register/register.html", {"form":form})