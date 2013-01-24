from datetime import datetime

from django.http import HttpResponseNotFound

from annoying.decorators import render_to

from gatherings.conference.models import (Event, Speaker, SESSION_TYPE_BREAK,
        SESSION_TYPE_TALK, SESSION_TYPE_LIGHTNING_TALK)
from gatherings.news.models import Post


@render_to('conference/home.html')
def home(request):
    page = 'home'
    return locals()


@render_to('conference/event.html')
def event(request, year):
    try:
        event = Event.objects.get(start__year=year)
    except Event.DoesNotExist:
        return HttpResponseNotFound('<h1>404 Not Found</h1>')
    page = 'sessions'

    return locals()


@render_to('conference/session.html')
def session(request, session_id):
    session = Session.objects.get(pk=session_id)
    page = 'sessions'


@render_to('conference/speakers.html')
def speakers(self):
    now = datetime.now()
    try:
        event = Event.objects.get(start__year=now.year)
    except Event.DoesNotExist:
        return HttpResponseNotFound('<h1>404 Not Found</h1>')
    speakers = Speaker.objects.filter(session__event=event).distinct()
    page = 'speakers'
    return locals()


@render_to('conference/speaker.html')
def speaker(request, speaker_id):
    speaker = Speaker.objects.get(pk=speaker_id)
    return locals()

@render_to('conference/speaker_edit.html')
def speaker_edit(request):
    return locals()