from django.contrib.auth.models import User
from django.db import models


class Page(models.Model):

    title = models.CharField(max_length=255)
    content = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, null=True, blank=True)
    updated_by = models.ForeignKey(User, null=True, 
            blank=True, related_name='updated_pages')

    def __unicode__(self):
        return self.title
