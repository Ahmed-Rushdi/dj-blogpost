from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def homepage(request: HttpRequest) -> HttpResponse:
    # return HttpResponse("Hello, world. You're at the myproject index.")
    return render(request, "home.html")


def about(request: HttpRequest) -> HttpResponse:
    # return HttpResponse("About myproject.")
    return render(request, "about.html")
