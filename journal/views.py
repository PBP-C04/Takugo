from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponseNotFound, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.http import JsonResponse
from journal.models import BookJournal, Book
from journal.forms import BookJournalForm

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
    book_journal_form = BookJournalForm()
    existing_journal = BookJournal.objects.filter(user=request.user, book=id)

    if (not existing_journal):
        context = {
        "name" : request.user.username,
        "book" : book_request,
        "book_journal_form" : book_journal_form,
    }

    else:    
        journals = BookJournal.objects.filter(user=request.user, book=id)
        context = {
            "name" : request.user.username,
            "book" : book_request,
            "book_journal_form" : book_journal_form,
            "journals" : journals,
        }
        
    return render(request, "my_journal.html", context)

def get_journal_json(request, id):
    journal_item = BookJournal.objects.filter(book=id, user=request.user)
    return HttpResponse(serializers.serialize('json', journal_item))

def all_journal_json(request):
    journal_item = BookJournal.objects.all()
    return HttpResponse(serializers.serialize('json', journal_item))

@csrf_exempt
def add_journal(request, id):
    if request.method == 'POST':
        user = request.user
        book = Book.objects.get(pk=id)
        notes = request.POST.get("notes")
        favorite_quotes = request.POST.get("favorite-quotes")
        rating = request.POST.get("rating")
        date_started = request.POST.get("date-started")
        date_finished = request.POST.get("date-finished")
        
        new_journal = BookJournal(user=user, book=book, notes=notes, favorite_quotes=favorite_quotes, rating=rating, date_started=date_started, date_finished=date_finished)
        new_journal.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

def delete_journal(request, id):
    journal = BookJournal.objects.filter(user=request.user, book=id)
    journal.delete()
    return JsonResponse({'message': 'Journal deleted successfully'}, status=200)