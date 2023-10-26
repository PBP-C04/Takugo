from django.urls import path
from bookreview.views import show_main, get_book_list, add_review, show_bookreview, review_json

app_name = "bookreview"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("api/book-list", get_book_list, name="get_book_list"),
    path("add-review/<int:book_id>", add_review, name="add_review"),
    path("show-bookreview/<int:book_id>", show_bookreview, name="show_bookreview"),
    path("review-json/<int:book_id>", review_json, name="review_json")
]
