from django.shortcuts import render
from .models import Post


# Create your views here.
def posts(request):
    return render(
        request,
        "posts/posts_list.html",
        {
            "posts": Post.objects.all().order_by("created_at").reverse(),
        },
    )
