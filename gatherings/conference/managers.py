from django.db import models
from django.db.models.query import QuerySet

from gatherings.conference.constants import SESSION_STATUS_PUBLISHED


class SessionQuerySet(QuerySet):

    @property
    def published(self):
        return self.filter(status=SESSION_STATUS_PUBLISHED)

    @property
    def ordered_for_event_display(self):
        return self.order_by('start')

class SessionManager(models.Manager):

    def get_query_set(self):
        return SessionQuerySet(self.model, using=self._db)

    def __getattr__(self, attr, *args):
        try:
            return getattr(self.__class__, attr, *args)
        except AttributeError:
            return getattr(self.get_query_set(), attr, *args)
