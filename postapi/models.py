from django.db import models
from django.utils import timezone


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=500, blank=False)
    description = models.TextField(blank=False)
    publish_date = models.DateTimeField(default=timezone.now)
    author = models.CharField(max_length=100, blank=False)

    class Meta:
        ordering = ['-publish_date']

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField(blank=False)
    author = models.CharField(max_length=100, blank=False)
    commented_on = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['commented_on']

    def __str__(self):
        return "comment on {}  post  by {}".format(self.post.title, self.author)
