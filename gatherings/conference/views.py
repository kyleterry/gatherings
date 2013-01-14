from django.http import HttpResponseNotFound

from annoying.decorators import render_to

from gatherings.conference.models import Event, Speaker
from gatherings.news.models import Post


def latest_news():
    news = Post.objects.published.order_by('-created_at')[:10]
    return news


@render_to('conference/home.html')
def home(request):
    news = latest_news()
    page = 'home'
    return locals()


@render_to('conference/event.html')
def event(request, year):
    try:
        event = Event.objects.get(start__year=year)
    except Event.DoesNotExist:
        return HttpResponseNotFound('<h1>404 Not Found</h1>')
    news = latest_news()
    page = 'sessions'
    return locals()


@render_to('conference/session.html')
def session(request, session_id):
    session = Session.objects.get(pk=session_id)
    page = 'sessions'
    news = latest_news()
    return locals()


@render_to('conference/speakers.html')
def speakers(self):
    speakers = Speaker.objects.all()
    news = latest_news()
    page = 'speakers'
    return locals()


@render_to('conference/speaker.html')
def speaker(request, speaker_id):
    speaker = Speaker.objects.get(pk=speaker_id)
    return locals()
