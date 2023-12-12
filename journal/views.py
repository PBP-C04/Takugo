from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponseNotFound, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.http import JsonResponse
from journal.models import BookJournal, Book
from journal.forms import BookJournalForm

import json

# Create your views here.
@login_required(login_url='/login')
def show_main(request: HttpRequest) -> HttpResponse:
    context = {
        "name": request.user.username,
    }
    
    if request.user.user_type == "I":
        return render(request, "unavailable.html", context)

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

@csrf_exempt
def get_journal_json(request, id):
    journal_item = BookJournal.objects.filter(book=id, user=request.user)
    return HttpResponse(serializers.serialize('json', journal_item))

def all_journal_json(request):
    journal_item = BookJournal.objects.all()
    return HttpResponse(serializers.serialize('json', journal_item))

@csrf_exempt
def add_journal(request, id):
    if request.method == 'POST':
        form = BookJournalForm(request.POST)
        if (form.is_valid()):
            user = request.user
            book = Book.objects.get(pk=id)
            notes = request.POST.get("notes")
            favorite_quotes = request.POST.get("favorite_quotes")
            rating = request.POST.get("rating")
            
            new_journal = BookJournal(user=user, book=book, notes=notes, favorite_quotes=favorite_quotes, rating=rating)
            new_journal.save()

            return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

@csrf_exempt
def delete_journal(request, id):
    journal = BookJournal.objects.filter(user=request.user, book=id)
    journal.delete()
    return JsonResponse({'message': 'Journal deleted successfully'}, status=200)

@csrf_exempt
def add_journal_flutter(request: HttpRequest, id: int) -> JsonResponse:
    if not request.user.is_authenticated:
        return JsonResponse({
            "status": False,
            "message": "Unauthorized"
        }, status=401)
    
    book = get_object_or_404(Book, pk=id)
    if request.method == 'POST':
        
        data = json.loads(request.body)
        
        new_journal = BookJournal.objects.create(
            user = request.user,
            book = book,
            notes = data["notes"],
            favorite_quotes = data["favorite_quotes"],
            rating = int(data["rating"]),
        )

        new_journal.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)