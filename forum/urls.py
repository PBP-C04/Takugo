from django.urls import path
from forum.views import create_post_flutter, create_reply, create_reply_flutter, detail, forum, create_post, reply, show_post_json, show_reply_json

app_name = "forum"

urlpatterns = [
    path('', forum, name="forum"),
    path('reply', reply, name="reply"),
    path('create_post', create_post, name="create_post"),
    path('create_reply/<int:pk>', create_reply, name="create_reply"),
    path('detail/<int:pk>', detail, name="detail"),
    path('reply_json/<int:pk>/', show_reply_json, name='show_reply_json'),
    path('post_json/', show_post_json, name='show_post_json'),
    path('create_post_flutter/', create_post_flutter, name="create_post_flutter"),
    path('create_reply_flutter/<int:pk>/', create_reply_flutter, name="create_reply_flutter"),
]
