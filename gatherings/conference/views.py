from django.http import HttpResponseNotFound

from annoying.decorators import render_to

from gatherings.conference.models import Event, Speaker
from gatherings.news.models import Post


@render_to('home.html')
def home(request):
    news = Post.objects.published
    return locals()


@render_to('conference/event.html')
def event(request, year):
    try:
        event = Event.objects.get(start__year=year)
    except Event.DoesNotExist:
        return HttpResponseNotFound('<h1>404 Not Found</h1>')
    return locals()


@render_to('conference/session.html')
def session(request, session_id):
    session = Session.objects.get(pk=session_id)
    return locals()


@render_to('conference/speaker.html')
def speaker(request, speaker_id):
    speaker = Speaker.objects.get(pk=speaker_id)
    return locals()
