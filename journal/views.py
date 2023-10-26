from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponseNotFound, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from journal.models import BookJournal, Book

# Create your views here.
@login_required(login_url='/login')
def show_main(request: HttpRequest) -> HttpResponse:
    context = {
        "name": request.user.username,
    }

    return render(request, "journal.html", context)

@csrf_exempt
def add_journal(request):
    if request.method == 'POST':
        notes = request.POST.get("notes")
        favorite_quotes = request.POST.get("favorite_quotes")
        rating = request.POST.get("rating")
        user = request.user

        # book = models.OneToOneField(Book, on_delete=models.CASCADE)

        new_journal = BookJournal(notes=notes, favorite_quotes=favorite_quotes, rating=rating, user=user)
        new_journal.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

def get_book_title(book_id):
    try:
        book = Book.objects.get(pk=book_id)
        return book.title
    except Book.DoesNotExist:
        return "Book Title Not Found"

# def get_journal(request: HttpRequest) -> HttpResponse:
#     journal = BookJournal.objects.filter(user=request.user)
#     return HttpResponse(serializers.serialize("json", journal))

