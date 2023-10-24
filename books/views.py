from django.core import serializers
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from books.models import Book, BoughtBook

# Create your views here.
def show_main(request: HttpRequest) -> HttpResponse:
    context = {
        "name": "Guest",
    }

    if request.user.is_authenticated:
        context["name"] = request.user.username

    return render(request, "books.html", context)


def get_book_list(request: HttpRequest) -> HttpResponse:
    filter = request.GET.get("filter")
    books = Book.objects.all()
    if filter != "none":
        books = books.filter(book_type=filter)
    
    return HttpResponse(serializers.serialize("json", books))


def get_book_bought(request: HttpRequest) -> HttpResponse:
    books = BoughtBook.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", books))


@csrf_exempt
def buy_book(request: HttpRequest, id: int) -> HttpResponse:
    pass
