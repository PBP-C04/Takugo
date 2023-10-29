from django.shortcuts import render
from forum.forms import PostForm
from forum.models import Post, Comment, Reply
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.contrib.auth.decorators import login_required
from main.models import TakugoUser
from django.shortcuts import get_object_or_404

# Create your views here.

def forum(request):
    if request.method=="POST":   
        user = TakugoUser.objects.filter(user=request.user)
        content = request.POST.get('content','')
        post = Post(user1=user, post_content=content)
        post.save()
        alert = True
        return render(request, "forum.html", {'alert':alert})
    posts = Post.objects.all()
    return render(request, "forum.html", {'posts':posts})

def posts(request):
    posts = Post.objects.filter(approved=True)
    context = {
        "posts": posts,
        "title": "Takugo: Posts"
    }

    return render(request, "posts.html", context)


@login_required
def create_post(request):
    print(TakugoUser.objects.get(user=request.user))
    context = {}
    form = PostForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            print("\n\n its valid")
            author = TakugoUser.objects.get(user=request.user)
            new_post = form.save(commit=False)
            new_post.user = author
            new_post.save()
            form.save_m2m()
            return redirect("home")
    context.update({
        "form": form,
        "title": "Takugo: Create New Post"
    })
    return render(request, "create_post.html", context)

def detail(request):
    post = get_object_or_404(Post)
    if request.user.is_authenticated:
        author = TakugoUser.objects.get(user=request.user)
    
    if "comment-form" in request.POST:
        comment = request.POST.get("comment")
        new_comment, created = Comment.objects.get_or_create(user=author, content=comment)
        post.comments.add(new_comment.id)

    if "reply-form" in request.POST:
        reply = request.POST.get("reply")
        commenr_id = request.POST.get("comment-id")
        comment_obj = Comment.objects.get(id=commenr_id)
        new_reply, created = Reply.objects.get_or_create(user=author, content=reply)
        comment_obj.replies.add(new_reply.id)

