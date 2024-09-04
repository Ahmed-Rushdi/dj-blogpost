from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    slug = models.SlugField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    banner = models.ImageField(default="fallback.png", blank=True)

    def __str__(self) -> str:
        return self.title
