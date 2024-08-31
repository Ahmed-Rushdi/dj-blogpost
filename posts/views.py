from django.shortcuts import render


# Create your views here.
def posts(request):
    return render(
        request,
        "posts/posts_list.html",
        {
            "posts": [
                "Post 1",
                "Post 2",
                "Post 3",
                "Post 4",
                "Post 5",
                "Post 6",
                "Post 7",
                "Post 8",
                "Post 9",
                "Post 10",
            ]
        },
    )
