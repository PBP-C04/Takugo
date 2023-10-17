from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from main.forms import RegisterForm, ChangeForm
from main.models import TakugoUser

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = RegisterForm
    form = ChangeForm
    model = TakugoUser
    list_display = ["username","user_type",]

admin.site.register(TakugoUser, CustomUserAdmin)
