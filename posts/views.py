from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from .models import Post


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


def create_post(request: HttpRequest) -> HttpResponse:
    user = request.user
    if user.is_anonymous:
        return redirect("users:login")
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
