from django.urls import path
from main.views import show_main, register_user, login_user, logout_user, settings, coming_sson

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("register/", register_user, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("settings/", settings, name="settings"),
    path("coming-soon/", coming_sson, name="coming-soon"),
]
