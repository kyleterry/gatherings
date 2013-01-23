from django.db import models


class SessionManager(models.Manager):

    @property
    def ordered_for_event_display(self):
        return self.order_by('start')

