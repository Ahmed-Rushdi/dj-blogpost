from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.decorators import login_required
from . import forms


# Create your views here.
def posts(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        "posts/posts_list.html",
        {
            "posts": Post.objects.all().order_by("created_at").reverse(),
        },
    )


def post_page(request: HttpRequest, slug: str) -> HttpResponse:
    return render(
        request,
        "posts/post_page.html",
        {
            "post": Post.objects.get(slug=slug),
        },
    )


@login_required(login_url="users:login")
def create_post(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("posts:list")
    else:
        form = forms.CreatePost()
    print("FORM:", form)
    return render(
        request,
        "posts/create_post.html",
        {
            "form": form,
        },
    )
