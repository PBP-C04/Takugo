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

@login_required(login_url='/login')
def show_journal(request, id):
    book_request = Book.objects.get(pk=id)

    if (BookJournal.DoesNotExist):
        context = {
        "name" : request.user.username,
        "book" : book_request,
        }

    else:    
        journals = BookJournal.objects.get(pk=id)
        context = {
            "name" : request.user.username,
            "book" : book_request,
            "journals" : journals,
        }
        
    return render(request, "my_journal.html", context)

def get_journal_json(request, id):
    journal_item = BookJournal.objects.filter(pk=id)
    return HttpResponse(serializers.serialize('json', journal_item))

@csrf_exempt
def add_journal(request, id):
    if request.method == 'POST':
        book = Book.objects.get(pk=id)
        notes = request.POST.get("notes")
        favorite_quotes = request.POST.get("favorite-quotes")
        rating = request.POST.get("rating")
        user = request.user

        new_journal = BookJournal(book=book, notes=notes, favorite_quotes=favorite_quotes, rating=rating, user=user)
        new_journal.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()


