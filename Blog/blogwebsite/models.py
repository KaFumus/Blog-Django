from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Post(models.Model):
    class PostStatus(models.TextChoices):
        PROJECT = 'PR', 'Project'
        PUBLISHED = 'PB', 'Published'
    title = models.CharField(max_length=256)
    hashtags = models.CharField(max_length=256, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,
                              choices= PostStatus.choices,
                              default = PostStatus.PROJECT)
    class Meta:
        ordering = ['-publish']
        indexes = [models.Index(fields=['-publish'])]

    def __str__(self):
        return self.title