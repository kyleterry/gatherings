from django.db import models


class PostManager(models.Manager):

    @property
    def published(self):
        return self.filter(published=True)
