from django.contrib.auth.models import User
from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    start = models.DateTimeField()
    end = models.DateTimeField()

    def __unicode__(self):
        return self.name


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
    description = models.TextField()
    event = models.ForeignKey('Event')
    room = models.ForeignKey('Room', null=True, blank=True)
    speaker = models.ForeignKey('Speaker')
    start = models.DateTimeField()
    end = models.DateTimeField()

    def __unicode__(self):
        return self.name


class Speaker(models.Model):
    bio = models.TextField()
    user = models.ForeignKey(User)

    @property
    def full_name(self):
        return '{first_name} {last_name}'.format(
            first_name=self.user.first_name, last_name=self.user.last_name)

    def __unicode__(self):
        return self.full_name
