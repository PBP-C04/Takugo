from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.http import HttpResponseNotFound
from donate.models import *
from books.models import *
from donate.forms import DonateForm
from main.models import TakugoUser

import json


# Create your views here.

@login_required(login_url='/login')
def show_donatepage(request):
    user = TakugoUser.objects.get(id=request.user.id)
    # return HttpResponse(serializers.serialize("json", books))

    donate_form = DonateForm()

    context = {
        'name': user.username,
        'user_type': user.user_type,
        'donate_form': donate_form,
    }
    
    if user.user_type == 'U':
        lembaga = TakugoUser.objects.filter(user_type='I')
        bought_books = BoughtBook.objects.filter(user=request.user).values("book")
        books = Book.objects.filter(pk__in=bought_books)
        context['books'] = books
        context['lembaga'] = lembaga

    return render(request, 'showdonate.html', context)


@csrf_exempt
def add_donate(request):
    if request.method == "POST":        
        donatur = request.user
        book = request.POST['book']
        book = Book.objects.get(pk=book)
        lembaga = request.POST['lembaga']
        lembaga = TakugoUser.objects.get(pk=lembaga)
        kondisi = request.POST['kondisi']
        donate = BookDonate(donatur=donatur, book=book, lembaga=lembaga, kondisi=kondisi)
        donate.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

def show_donate_user(request):
    book_donate = BookDonate.objects.filter(donatur=request.user)
    donated_list = []
    for book in book_donate:
        kondisi = book.kondisi
        lembaga = TakugoUser.objects.get(pk=book.lembaga.id).username
        title = Book.objects.get(pk=book.book.id).title
        donated_date = str(book.tanggal_donasi)
        donated_list.append({"title":title,"kondisi":kondisi,"lembaga":lembaga,"donated_date":donated_date})

    data = json.dumps(donated_list)
    return HttpResponse(data, content_type='application/json')

def show_donate_lembaga(request):
    book_donate = BookDonate.objects.filter(lembaga=request.user)
    donated_list = []
    for book in book_donate:
        kondisi = book.kondisi
        donatur = TakugoUser.objects.get(pk=book.donatur.id).username
        title = Book.objects.get(pk=book.book.id).title
        donated_date = str(book.tanggal_donasi)
        donated_list.append({"title":title,"kondisi":kondisi,"donatur":donatur,"donated_date":donated_date})

    data = json.dumps(donated_list)
    return HttpResponse(data, content_type='application/json')