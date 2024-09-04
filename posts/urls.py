from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path("", views.posts, name="list"),
    path("create/", views.create_post, name="create"),
    path("<slug:slug>", views.post_page, name="page"),
]
