from pickle import TRUE

from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

"""
class Post:
    id int
    title str(50)
    content text
    created datetime
"""

User = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ["-created"]
