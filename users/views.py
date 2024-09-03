from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from django.http import HttpRequest, HttpResponse

# Create your views here.


def register(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("posts:list")
        else:
            print(form.errors)
    else:
        form = UserCreationForm()
    return render(request, "users/register.html", {"form": UserCreationForm()})
