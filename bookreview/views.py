from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, HttpResponseForbidden
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from bookreview.models import BookReview
from books.models import Book
from django.http import JsonResponse
from main.models import TakugoUser
from bookreview.forms import BookReviewForm
from books.views import get_book_list
import json, datetime

# View yang menangani tampilan utama
def show_main(request):
    context = {
        "name": "Guest",
    }

    if request.user.is_authenticated:
        context["name"] = request.user.username
        
        if request.user.user_type == "I":
            return render(request, "unavailable.html", context)

    return render(request, "bookreview.html", context)

# View yang menangani penambahan review
@login_required
def add_review(request, book_id):
    if request.method == 'POST':
        form = BookReviewForm(request.POST)  # Gunakan formulir Django
        if form.is_valid():
            comment = form.cleaned_data['comment']
            rating = form.cleaned_data['rating']

            book = Book.objects.get(pk=book_id)
            review = BookReview(
                comment=comment,
                rating=rating,
                user=request.user,
                book=book
            )
            review.save()
            return HttpResponse(b"CREATED", status=201)
    
    return HttpResponseNotFound()


def show_bookreview(request, book_id):
    book_to_review = Book.objects.get(pk=book_id)
    bookreview_data = BookReview.objects.filter(book=book_id)
    data_count = bookreview_data.count()
    review_form = BookReviewForm()
    
    if request.user.is_authenticated:
        user_type_status = request.user.user_type
        name = request.user.username
    else:
        user_type_status = "X"
        name = "Guest"

    context = {
        'book_to_review': book_to_review,
        'list_of_review': bookreview_data,
        'name': name,
        'user_status': user_type_status,
        'data_count': data_count,
        'review_form': review_form
    }

    return render(request, 'showreview.html', context)


def review_json(request, book_id):
    data = BookReview.objects.filter(book=book_id)
    return HttpResponse(serializers.serialize('json', data))

@login_required
def delete_review(request, id):
    try:
        review = BookReview.objects.get(pk=id)
        
        # Periksa apakah pengguna saat ini adalah pemilik ulasan
        if request.user == review.user:
            review.delete()
            return JsonResponse({'message': 'Review deleted successfully'}, status=200)
        else:
            return JsonResponse({'message': 'You are not authorized to delete this review'}, status=403)
    except BookReview.DoesNotExist:
        return JsonResponse({'message': 'Review not found'}, status=404)

def get_data_count(request, book_id):
    review_count = BookReview.objects.filter(book=book_id).count()
    return HttpResponse(str(review_count))

def update_data_count(request, book_id):
    if request.method == 'GET':
        review_count = BookReview.objects.filter(book=book_id).count()
        return HttpResponse(str(review_count))
    
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import BookReview, Book

@require_POST
def add_review_flutter(request):
    data = json.loads(request.body)

    # Get the book using book_id or return 404 if not found
    book_id=data.get('bookID')
    book = get_object_or_404(Book, pk=book_id)

    new_review = BookReview.objects.create(
        user=request.user,
        name=data["name"],
        comment=data["comment"],
        rating=int(data["rating"]),
        book=book,  # Associate the review with the specific book
        date=datetime.now,
    )

    new_review.save()
    
    return JsonResponse({"status": "success"}, status=200)

    
def get_reviews_json_by_req_id(request, book_id):
    user = request.user
    book = get_object_or_404(Book, pk=book_id)
    reviews = BookReview.objects.filter(user=user, book=book)
    return HttpResponse(serializers.serialize("json", reviews), content_type="application/json")

def get_other_review_json(request, book_id):
    user = request.user
    book = get_object_or_404(Book, pk=book_id)
    reviews = BookReview.objects.filter(book=book).exclude(user)
    return HttpResponse(serializers.serialize("json", reviews), content_type="application/json")


