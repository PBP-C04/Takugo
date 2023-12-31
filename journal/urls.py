from django.urls import path
from journal.views import show_main, add_journal, show_journal, get_journal_json, all_journal_json, delete_journal, add_journal_flutter
from books.views import get_book_list, get_book_bought

app_name = 'journal'

urlpatterns = [
    path('', show_main, name='show_main'),
    path("api/book-list", get_book_list, name="get_book_list"),
    path("api/book-bought", get_book_bought, name="get_book_bought"),
    path("add_journal/<int:id>/", add_journal, name="add_journal"),
    path("show_journal/<int:id>/", show_journal, name="show_journal"),
    path("all_journal_json/", all_journal_json, name="all_journal_json"),
    path("get_journal_json/<int:id>/", get_journal_json, name="get_journal_json"),
    path("delete_journal/<int:id>/", delete_journal, name="delete_journal"),
    path("add_journal_flutter/<int:id>/", add_journal_flutter, name="add_journal_flutter"),
]