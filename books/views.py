from django.core import serializers
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

from books.models import Book, BoughtBook
from books.forms import BookForm

# Create your views here.
def show_main(request: HttpRequest) -> HttpResponse:
    context = {
        "name": "Guest",
        "form": BookForm(),
    }

    if request.user.is_authenticated:
        if request.user.user_type == "I":
            return render(request, "unavailable.html", {})
        
        context["name"] = request.user.username

    return render(request, "books.html", context)


def get_book_list(request: HttpRequest) -> HttpResponse:
    filter = request.GET.get("filter")
    books = Book.objects.all()
    if filter != "none":
        books = books.filter(book_type=filter)
    
    return HttpResponse(serializers.serialize("json", books))


def get_book_bought(request: HttpRequest) -> HttpResponse:
    filter = request.GET.get("filter")
    bought_books = BoughtBook.objects.filter(user=request.user).values("book")
    books = Book.objects.filter(pk__in=bought_books)
    if filter != "none":
        books = books.filter(book_type=filter)
    return HttpResponse(serializers.serialize("json", books))


@require_POST
@csrf_exempt
def buy_book(request: HttpRequest, id: int) -> HttpResponse:
    book = get_object_or_404(Book, pk=id)
    bought_books = BoughtBook.objects.filter(user=request.user).values("book")
    if bought_books.filter(book=book.pk).exists():
        return HttpResponse(b"Already bought this book", status=503)
    
    amt = request.POST.get("amount")
    amt = amt if amt else 1
    bought_book = BoughtBook(
        book=book, 
        user=request.user, 
        amount=amt
    )
    bought_book.save()
    return HttpResponse(b"Successfully bought book", status=201)
