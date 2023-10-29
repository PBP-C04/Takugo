from django.core import serializers
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET
from django.contrib.auth.decorators import login_required

from books.models import Book, BoughtBook
from books.forms import BookForm

# Create your views here.
@require_GET
def show_main(request: HttpRequest) -> HttpResponse:
    context = {
        "name": "Guest",
        "form": BookForm(),
    }

    if request.user.is_authenticated:
        context["name"] = request.user.username
        
        if request.user.user_type == "I":
            return render(request, "unavailable.html", context)

    return render(request, "books.html", context)


@require_GET
def get_book_list(request: HttpRequest) -> HttpResponse:
    filter = request.GET.get("filter", "none")
    books = Book.objects.all()
    if filter != "none":
        books = books.filter(book_type=filter)
    
    return HttpResponse(serializers.serialize("json", books), content_type="application/json")


@require_GET
def get_book_bought(request: HttpRequest) -> HttpResponse:
    if not request.user.is_authenticated:
        return HttpResponse(b"Unauthorized", status=401)
    
    filter = request.GET.get("filter", "none")
    bought_books = BoughtBook.objects.filter(user=request.user).values("book")
    books = Book.objects.filter(pk__in=bought_books)
    if filter != "none":
        books = books.filter(book_type=filter)
    return HttpResponse(serializers.serialize("json", books), content_type="application/json")


@require_POST
@csrf_exempt
def buy_book(request: HttpRequest, id: int) -> HttpResponse:
    if not request.user.is_authenticated:
        return HttpResponse(b"Unauthorized", status=401)

    amt = request.POST.get("amount")
    if amt is None:
        return HttpResponse(b"Amount not found", status=400)
    
    book = get_object_or_404(Book, pk=id)
    bought_books = BoughtBook.objects.filter(user=request.user).values("book")
    if bought_books.filter(book=book.pk).exists():
        return HttpResponse(b"Already bought this book", status=403)
    
    if amt == "":
        amt = 1

    else:
        try:
            amt = int(amt)
        except ValueError:
            return HttpResponse(b"Amount must be an integer between 1-20", status=400)

    if amt <= 0 or amt > 20:
        return HttpResponse(b"Amount must be between 1-20", status=400)

    bought_book = BoughtBook(
        book=book, 
        user=request.user, 
        amount=amt
    )
    bought_book.save()
    return HttpResponse(b"Successfully bought book", status=201)
