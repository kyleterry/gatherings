from django.conf.urls import patterns, url

urlpatterns = patterns('gatherings.conference.views',
    url(r'^$', 'home', name='home'),
    url(r'^events/(?P<year>\d{4})/', 'event', name='conference_event'),
    url(r'^speaker/(?P<speaker_id>\d)/', 'speaker', name='conference_speaker'),
)
