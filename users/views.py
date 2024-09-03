from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.


def register(request: HttpRequest) -> HttpResponse:
    return render(request, "users/register.html")
