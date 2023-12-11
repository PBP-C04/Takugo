from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt

from main.models import TakugoUser


@csrf_exempt
def login(request: HttpRequest) -> JsonResponse:
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            
            return JsonResponse({
                "username": user.username,
                "status": True,
                "message": "Login success!"
            }, status=200)
        else:
            return JsonResponse({
                "status": False,
                "message": "Login failed, account is deactivated."
            }, status=401)

    else:
        return JsonResponse({
            "status": False,
            "message": "Incorrect username or password"
        }, status=401)


@csrf_exempt
def logout(request: HttpRequest) -> JsonResponse:
    username = request.user.username
    try:
        auth_logout(request)
        return JsonResponse({
            "username": username,
            "status": True,
            "message": "Logout success!"
        }, status=200)
    
    except:
        return JsonResponse({
            "status": False,
            "message": "Logout failed!"
        }, status=401)


@csrf_exempt
def register(request: HttpRequest) -> JsonResponse:
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user_type = request.POST["user_type"]
        
        user = TakugoUser.objects.create_user(
            username=username,
            password=password,
            # user_type=user_type
        )
        user.user_type = user_type
        user.save()
        return JsonResponse({
            "status": True,
            "message": "Successfully created an account!"
        }, status=200)
    
    return JsonResponse({
        "status": False,
        "message": "Method not allowed"
    }, status=405)
