from django.urls import path
from bookreview.views import show_main, get_book_list, add_review, show_bookreview, review_json, delete_review, get_data_count, update_data_count, add_review_flutter
from bookreview.views import get_other_review_json, get_reviews_json_by_req_id

app_name = "bookreview"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("api/book-list", get_book_list, name="get_book_list"),
    path("add-review/<int:book_id>", add_review, name="add_review"),
    path("show-bookreview/<int:book_id>", show_bookreview, name="show_bookreview"),
    path("review-json/<int:book_id>", review_json, name="review_json"),
    path("delete-review/<int:id>", delete_review, name="delete_review"),
    path('data_count/<int:book_id>/', get_data_count, name='data_count'),
    path('update_data_count/<int:book_id>/', update_data_count, name='update_data_count'),
    path('add-review-flutter/', add_review_flutter, name="add_review_flutter"),
    path('get-other-review-json/<int:book_id>/', get_other_review_json, name="get_other_review_json"),
    path('get-reviews-json-by-req-id/<int:book_id>/', get_reviews_json_by_req_id, name="get_reviews_json_by_req_id")
]