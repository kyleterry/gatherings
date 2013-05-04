from datetime import timedelta

from django.contrib.auth.models import User
from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, Adjust

from gatherings.conference.managers import SessionManager
from gatherings.conference.constants import (SESSION_TYPE_TALK,
        SESSION_TYPE_LIGHTNING_TALK, SESSION_TYPE_BREAK, SESSION_TYPE_CHOICES,
        SESSION_STATUS_DRAFT, SESSION_STATUS_PUBLISHED, SESSION_STATUS_CHOICES)


class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    start = models.DateTimeField()
    end = models.DateTimeField()

    def __unicode__(self):
        return self.name

    def get_datetimes(self):
        return [self.start + timedelta(days=x) for x in range(0,
            (self.end.date() - self.start.date()).days + 1)]

    @property
    def sessions_by_days_struct(self):
        sessions = {}
        for dt in self.get_datetimes():
            sessions[dt] = self.session_set.filter(
                status=SESSION_STATUS_PUBLISHED,
                start__startswith=dt.date()).order_by('start')
        return sessions


class Track(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class Room(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class Session(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    event = models.ForeignKey('Event')
    room = models.ForeignKey('Room', null=True, blank=True)
    speakers = models.ManyToManyField('Speaker', null=True, blank=True)
    session_type = models.IntegerField(default=SESSION_TYPE_TALK,
                                       choices=SESSION_TYPE_CHOICES)
    status = models.IntegerField(default=SESSION_STATUS_DRAFT,
                                 choices=SESSION_STATUS_CHOICES)
    start = models.DateTimeField(null=True, blank=True)
    end = models.DateTimeField(null=True, blank=True)

    objects = SessionManager()

    def __unicode__(self):
        return self.name

    @property
    def is_break(self):
        return self.session_type == SESSION_TYPE_BREAK

    @property
    def is_talk(self):
        return self.session_type == SESSION_TYPE_TALK

    @property
    def is_lightning_talk(self):
        return self.session_type == SESSION_TYPE_LIGHTNING_TALK

    @property
    def is_published(self):
        return self.status == SESSION_STATUS_PUBLISHED


class Speaker(models.Model):
    bio = models.TextField()
    user = models.ForeignKey(User, null=True, blank=True)
    tags = models.ManyToManyField('SpeakerTag', null=True, blank=True)
    image = models.ImageField(upload_to='speaker_images', null=True, blank=True)
    image_thumbnail = ImageSpecField([Adjust(contrast=1.2, sharpness=1.1),
                                     ResizeToFill(130, 130)],
                                     image_field='image',
                                     format='PNG',
                                     options={'quality': 90})
    events = models.ManyToManyField('Event', null=True, blank=True)

    @property
    def full_name(self):
        return '{first_name} {last_name}'.format(
            first_name=self.user.first_name, last_name=self.user.last_name)

    def __unicode__(self):
        return self.full_name


class SpeakerTag(models.Model):

    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name
