from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify


class Page(models.Model):

    title = models.CharField(max_length=255)
    content = models.TextField(null=True)
    slug = models.SlugField(blank=True)
    show_title = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, null=True, blank=True)
    updated_by = models.ForeignKey(User, null=True,
            blank=True, related_name='updated_pages')

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Page, self).save(*args, **kwargs)
