from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    author = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.description

    class Meta:
        ordering = ['created']

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={'pk': self.pk})