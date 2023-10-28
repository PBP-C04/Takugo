from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.http import HttpResponseNotFound
from Takugo.donate.models import *
from Takugo.books.models import *
from Takugo.donate.forms import DonateForm
from main.models import TakugoUser


# Create your views here.

@login_required(login_url='/login')
def show_donatepage(request):

    user = TakugoUser.objects.filter(user=request.user)
    lembaga = TakugoUser.objects.filter(user_type='I')
    books_lembaga = BookDonate.objects.filter(lembaga=request.user) 
    books_user = BoughtBook.objects.filter(user=request.user)
    donate_form = DonateForm()

    context = {
        'name' : user.username,
        'type' : user.user_type,
        'lembaga' : lembaga,
        'books_user' : books_user,
        'donate_form' : donate_form,
        'books_lembaga' : books_lembaga
    }

    return render(request, 'donate/showdonate.html', context)

@csrf_exempt
def add_donate(request):
    if request.method == "POST":
        
        donate = BookDonate (
            donatur = request.user,
            book = request.POST['book'],
            lembaga = request.POST['lembaga'],
            kondisi = request.POST['kondisi'],
        )

        donate.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

def show_donate_user(request):
    books = BookDonate.objects.filter(user=request.user)
    data = serializers.serialize('json', books)
    return HttpResponse(data, content_type='application/json')

def show_donate_lembaga(request):
    books = BookDonate.objects.filter(lembaga=request.user)
    data = serializers.serialize('json', books)
    return HttpResponse(data, content_type='application/json')