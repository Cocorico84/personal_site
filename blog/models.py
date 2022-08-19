from django.db import models
from django.conf import settings


class Article(models.Model):
    title = models.CharField(max_length=64)
    subject = models.TextField()
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="authors"
    )
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
