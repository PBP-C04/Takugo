from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserChangeForm

from main.forms import RegisterForm, ChangeForm
from main.models import TakugoUser


def show_main(request: HttpRequest) -> HttpResponse:
    return render(request, "main.html", {})


def register_user(request: HttpRequest) -> HttpResponse | HttpResponseRedirect:
    form = RegisterForm()
    
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("main:login")
    
    context = {"form": form}
    return render(request, "register.html", context)


def login_user(request: HttpRequest) -> HttpResponse | HttpResponseRedirect:
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            redirect_url = request.GET.get("next", None)
            if redirect_url:
                return redirect(redirect_url)
            
            return HttpResponseRedirect(reverse("main:show_main"))
        
        else:
            messages.info(request, "Invalid username or password.")
    
    context = {}
    return render(request, "login.html", context)


def logout_user(request: HttpRequest) -> HttpResponseRedirect:
    logout(request)
    return HttpResponseRedirect(reverse("main:show_main"))


def settings(request: HttpRequest) -> HttpResponse | HttpResponseRedirect:
    form = ChangeForm(instance=request.user)

    if request.method == "POST":
        form = ChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("main:show_main")
    
    context = {"form": form}
    return render(request, "settings.html", context)
