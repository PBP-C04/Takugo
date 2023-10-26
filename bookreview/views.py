from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from books.views import get_book_list
from django.core import serializers
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from bookreview.models import BookReview
from books.models import Book
from django.http import JsonResponse
from main.models import TakugoUser

# View yang menangani tampilan utama
def show_main(request):
    context = {
        "name": "Guest",
    }

    if request.user.is_authenticated:
        context["name"] = request.user.username

    return render(request, "bookreview.html", context)

# View yang menangani penambahan review
@login_required
def add_review(request, book_id):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        rating = request.POST.get('rating')
        
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
    user = request.user

    print(book_to_review.pk)

    context = {
        'book_to_review': book_to_review,
        'list_of_review': bookreview_data,
        'name': request.user.username,
        'user_status': request.user.user_type
    }

    return render(request, 'showreview.html', context)

def review_json(request, book_id):
    data = BookReview.objects.filter(pk=book_id)
    return HttpResponse(serializers.serialize('json', data))




