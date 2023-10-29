from django.urls import path
from forum.views import forum, create_post, detail, posts

app_name = "forum"

urlpatterns = [
    path('', forum, name="forum"),
    path('create_post', create_post, name="create_post"),
    path('detail', detail, name="detail"),
    path("posts", posts, name="posts"),
]
