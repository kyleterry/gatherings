from django.db import models
from django.utils.text import slugify

from gatherings.news.managers import PostManager


class Post(models.Model):

    title = models.CharField(max_length=255)
    content = models.TextField()
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField('Tag', null=True)

    objects = PostManager()

    def __unicode__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Tag, self).save(*args, **kwargs)

    def reslug(self):
        self.slug = slugify(self.name)
        self.save()

    def __unicode__(self):
        return self.name
