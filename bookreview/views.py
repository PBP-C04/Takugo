from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from books.views import get_book_list
from django.core import serializers
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, HttpResponseForbidden
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
    data_count = bookreview_data.count()
    
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
        'data_count': data_count
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
    
def get_review_count(request, book_id):
    review_count = BookReview.objects.filter(book=book_id).count()
    return JsonResponse({'count': review_count})

