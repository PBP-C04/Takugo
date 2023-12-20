from django.urls import path
from donate.views import *

app_name = "donate"

urlpatterns = [
    path('', show_donatepage, name="show_donatepage"),
    path('add_donate/', add_donate, name="add_donate"),
    path('show_donate_user/', show_donate_user, name="show_donate_user"),
    path('show_donate_lembaga/', show_donate_lembaga, name="show_donate_lembaga"),
    path('show_json_donate/', show_json_donate, name="show_json_donate"),
    path('show_json/', show_json, name="show_json"),
    path('add_donate_flutter/', add_donate_flutter, name="add_donate_flutter"),
    path('endpoint_for_books/', endpoint_for_books, name='endpoint_for_books'),
    path('endpoint_for_lembaga/', endpoint_for_lembaga, name='endpoint_for_donate'),
]
