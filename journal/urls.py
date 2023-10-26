from django.urls import path
from journal.views import show_main, add_journal, get_book_title
from books.views import get_book_list

app_name = 'journal'

urlpatterns = [
    path('', show_main, name='show_main'),
    path("api/book-list", get_book_list, name="get_book_list"),
    path("add_journal/", add_journal, name="add_journal"),
    path("get_book_title/", get_book_title, name="get_book_title")
    # path('add-journal/', add_journal, name='add_journal'),
    # path('get-journal/', get_journal, name='get_journal')
]