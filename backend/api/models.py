from django.db import models
from django.contrib.auth.models import User


class Comment(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")

    def __str__(self) -> str:
        return self.title

# Create your models here.
