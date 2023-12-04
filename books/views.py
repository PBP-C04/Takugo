import json

from django.core import serializers
from django.http import HttpRequest, HttpResponse, JsonResponse
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
    bought_books = BoughtBook.objects.filter(user=request.user)
    resp_json = []
    for bought_book in bought_books:
        if filter != "none" and book.book_type != filter:
            continue
    
        fields = {}
        fields["amount"] = bought_book.amount
        book = Book.objects.get(pk=bought_book.book.id)
        fields["title"] = book.title
        fields["score"] = book.score
        fields["volumes"] = book.volumes
        fields["image_url"] = book.image_url
        resp_json.append({"modal": "books.BoughtBook", "pk": book.id, "fields": fields})

    resp_json = json.dumps(resp_json)
    return HttpResponse(resp_json, content_type="application/json")


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


@csrf_exempt
def get_book_list_flutter(request: HttpRequest) -> JsonResponse:
    filter = request.GET.get("filter", "none")
    books = Book.objects.all()
    if filter != "none":
        books = books.filter(book_type=filter)
    
    return JsonResponse({
        "status": True,
        "books": serializers.serialize("json", books)
    }, status=200)


@csrf_exempt
def get_book_bought_flutter(request: HttpRequest) -> JsonResponse:
    if not request.user.is_authenticated:
        return JsonResponse({
            "status": False,
            "message": "Unauthorized"
        }, status=401)
    
    filter = request.GET.get("filter", "none")
    bought_books = BoughtBook.objects.filter(user=request.user)
    resp_json = []
    for bought_book in bought_books:
        if filter != "none" and book.book_type != filter:
            continue
    
        fields = {}
        fields["amount"] = bought_book.amount
        book = Book.objects.get(pk=bought_book.book.id)
        fields["title"] = book.title
        fields["score"] = book.score
        fields["volumes"] = book.volumes
        fields["image_url"] = book.image_url
        resp_json.append({"modal": "books.BoughtBook", "pk": book.id, "fields": fields})

    resp_json = json.dumps(resp_json)
    return JsonResponse({
        "status": True,
        "bought_books": resp_json
    }, status=200)


@csrf_exempt
def buy_book_flutter(request: HttpRequest, id: int) -> JsonResponse:
    if not request.user.is_authenticated:
        return JsonResponse({
            "status": False,
            "meesage": "Unauthorized"
        }, status=401)

    amt = request.POST.get("amount")
    if amt is None:
        return JsonResponse({
            "status": False,
            "message": "Amount not found"
        }, status=400)
    
    book = get_object_or_404(Book, pk=id)
    bought_books = BoughtBook.objects.filter(user=request.user).values("book")
    if bought_books.filter(book=book.pk).exists():
        return JsonResponse({
            "status": False,
            "message": "Already bought this book"
        }, status=403)
    
    if amt == "":
        amt = 1

    else:
        try:
            amt = int(amt)
        except ValueError:
            return JsonResponse({
                "status": False,
                "message": "Amount must be an integer between 1-20"
            }, status=400)

    if amt <= 0 or amt > 20:
        return JsonResponse({
            "status": False,
            "message": "Amount must be between 1-20"
        }, status=400)

    bought_book = BoughtBook(
        book=book, 
        user=request.user, 
        amount=amt
    )
    bought_book.save()
    return JsonResponse({
        "status": True,
        "message": "Successfully bought book"
    }, status=201)
