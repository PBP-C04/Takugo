from django.shortcuts import render
from forum.forms import PostForm, ReplyForm
from forum.models import Post, Reply
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.contrib.auth.decorators import login_required
from main.models import TakugoUser
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404
import json

# Create your views here.

def forum(request):
    if request.method=="POST":   
        user = TakugoUser.objects.filter(user=request.user)
        content = request.POST.get('content','')
        post = Post(user=user, post_content=content)
        post.save()
        alert = True
        return render(request, "forum.html", {'alert':alert})
    posts = Post.objects.all()
    return render(request, "forum.html", {'posts':posts})

@login_required(login_url='/login')
def create_post(request):
    context = {}
    form = PostForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            print("\n\n its valid")
            author = request.user
            new_post = form.save(commit=False)
            new_post.author = author
            new_post.save()
            form.save_m2m()
            return redirect("forum:forum")
    context.update({
        "form": form,
    })
    return render(request, "create_post.html", context)

def detail(request, pk):
    post = Post.objects.get(pk=pk)
    replies = Reply.objects.filter(post=post)
    context = {
        "replies" : replies,
        "post" : post,
    }
    return render(request, "detail.html", context)


def reply(request):
    if request.method=="POST":   
        user = TakugoUser.objects.filter(user=request.user)
        content = request.POST.get('content','')
        reply = Reply(user=user, post_content=content)
        reply.save()
        alert = True
        return render(request, "reply.html", {'alert':alert})
    replies = Reply.objects.all()
    return render(request, "reply.html", {'replies':replies})

@login_required(login_url='/login')
def create_reply(request, pk):    
    form = ReplyForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            print("\n\n its valid")
            author = request.user
            new_post = form.save(commit=False)
            new_post.author = author
            new_post.post = Post.objects.get(pk=pk)
            new_post.save()
            return redirect("forum:detail", pk=pk)
    context = {
        "form" : form,
    }
    return render(request, "create_reply.html", context)

def show_reply_json(request):
    data = Reply.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_post_json(request):
    data = Post.objects.all()

    return JsonResponse({
        "status": True,
        "post": serializers.serialize("json", data)
    }, status=200)

@csrf_exempt
def create_post_flutter(request, id):
    if not request.user.is_authenticated:
        return JsonResponse({
            "status": False,
            "message": "Unauthorized"
        }, status=401)
    
    post = get_object_or_404(Post, pk=id)
    if request.method == 'POST':
        
        data = json.loads(request.body)
        
        new_journal = Post.objects.create(
            user = request.user,
            post = post,
            title = data["title"],
            content = data["content"],
        )

        new_journal.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)
