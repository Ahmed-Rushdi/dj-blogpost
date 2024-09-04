from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.decorators import login_required


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
        data = request.POST.dict()
        data.pop("csrfmiddlewaretoken"), data.pop("banner")
        if "banner" in request.FILES:
            data["banner"] = request.FILES["banner"]
        print("DATA: ", data)
        print("FILES: ", request.FILES)
        Post.objects.create(**data)
        return redirect("posts:list")
    else:
        return render(
            request,
            "posts/create_post.html",
        )
