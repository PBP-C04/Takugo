from django.urls import path
from forum.views import create_reply, detail, forum, create_post, reply, show_reply_json

app_name = "forum"

urlpatterns = [
    path('', forum, name="forum"),
    path('reply', reply, name="reply"),
    path('create_post', create_post, name="create_post"),
    path('create_reply/<int:pk>', create_reply, name="create_reply"),
    path('detail/<int:pk>', detail, name="detail"),
    path('json/', show_reply_json, name='show_json'),
]
