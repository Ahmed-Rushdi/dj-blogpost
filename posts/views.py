from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
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
