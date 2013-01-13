from django.db import models


class Post(models.Model):

    title = models.CharField(max_length=255)
    content = models.TextField()
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField('Tag')


class Tag(models.Model):
    name = models.CharField(max_length=255)
