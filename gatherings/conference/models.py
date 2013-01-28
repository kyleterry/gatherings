from datetime import timedelta

from django.contrib.auth.models import User
from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, Adjust

from gatherings.conference.managers import SessionManager


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


SESSION_TYPE_TALK = 1
SESSION_TYPE_LIGHTNING_TALK = 2
SESSION_TYPE_BREAK = 3
SESSION_TYPE_CHOICES = (
    (SESSION_TYPE_TALK, 'Talk'),
    (SESSION_TYPE_LIGHTNING_TALK, 'Lightning Talk'),
    (SESSION_TYPE_BREAK, 'Break'),
)

class Session(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    event = models.ForeignKey('Event')
    room = models.ForeignKey('Room', null=True, blank=True)
    speakers = models.ManyToManyField('Speaker', null=True, blank=True)
    session_type = models.IntegerField(default=SESSION_TYPE_TALK,
                                       choices=SESSION_TYPE_CHOICES)
    start = models.DateTimeField()
    end = models.DateTimeField()

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


class Speaker(models.Model):
    bio = models.TextField()
    user = models.ForeignKey(User)
    tags = models.ManyToManyField('SpeakerTag', null=True, blank=True)
    image = models.ImageField(upload_to='speaker_images', null=True, blank=True)
    image_thumbnail = ImageSpecField([Adjust(contrast=1.2, sharpness=1.1),
                                     ResizeToFill(130, 130)],
                                     image_field='image',
                                     format='PNG',
                                     options={'quality': 90})

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
