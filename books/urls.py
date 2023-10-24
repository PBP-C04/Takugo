from django.urls import path
from books.views import show_main, get_book_list, get_book_bought, buy_book

app_name = "books"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("api/book-list", get_book_list, name="get_book_list"),
    path("api/book-bought", get_book_bought, name="get_book_bought"),
    path("buy-book/<int:id>", buy_book, name="buy_book"),
]