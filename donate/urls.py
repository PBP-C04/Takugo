from django.urls import path
from donate.views import *

app_name = "donate"

urlpatterns = [
    path('', show_donatepage, name="donate"),
    path('add_donate/', add_donate, name="add_donate"),
    path('show_donate_user/', show_donate_user, name="show_donate_user"),
    path('show_donate_lembaga/', show_donate_lembaga, name="show_donate_lembaga"),
]
