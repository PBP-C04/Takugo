from django.urls import path
from books.views import show_main, get_book_list, get_book_bought, buy_book, \
                        get_book_list_flutter, get_book_bought_flutter, buy_book_flutter

app_name = "books"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("api/book-list", get_book_list, name="get_book_list"),
    path("api/book-bought", get_book_bought, name="get_book_bought"),
    path("buy-book/<int:id>", buy_book, name="buy_book"),
    path("api/book-list-flutter/", get_book_list_flutter, name="get_book_list_flutter"),
    path("api/book-bought-flutter/", get_book_bought_flutter, name="get_book_bought_flutter"),
    path("buy-book-flutter/<int:id>/", buy_book_flutter, name="buy_flutter"),
]