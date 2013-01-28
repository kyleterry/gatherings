from datetime import datetime

from django.http import HttpResponseNotFound

from annoying.decorators import render_to

from gatherings.conference.models import (Event, Speaker, SESSION_TYPE_BREAK,
        SESSION_TYPE_TALK, SESSION_TYPE_LIGHTNING_TALK)
from gatherings.conference.forms import SpeakerForm
from gatherings.news.models import Post
from gatherings.cms.models import Page


@render_to('conference/home.html')
def home(request):
    page = 'home'
    home_page, created = Page.objects.get_or_create(title='Home Page')
    if created:
        home_page.content = 'This is your temporary home page. Edit it in the admin.'
        home_page.save()
    return locals()


@render_to('conference/event.html')
def event(request, year):
    try:
        event = Event.objects.get(start__year=year)
    except Event.DoesNotExist:
        if Event.objects.all().exists():
            try:
                event = Event.objects.all().order_by('-start')[0]
            except IndexError:
                event = None
        #return HttpResponseNotFound('<h1>404 Not Found</h1>')
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
    if not Speaker.objects.filter(user=request.user).exists():
        Speaker.objects.create(user=request.user)
    speaker_form = SpeakerForm(instance=Speaker.objects.get(user=request.user))
    if request.method == 'POST':
        speaker_form = SpeakerForm(data=request.POST or None,
                                instance=Speaker.objects.get(user=request.user))
        if speaker_form.is_valid():
            speaker_form.save()
            profile_saved = True
    return locals()
