from django.conf.urls import patterns, url

urlpatterns = patterns('gatherings.conference.views',
    url(r'^$', 'home', name='home'),
    url(r'^events/(?P<year>\d{4})/', 'event', name='conference_event'),
    url(r'^speakers/(?P<speaker_id>\d+)', 'speaker', name='conference-speaker'),
    url(r'^speakers/$', 'speakers', name='conference_speakers'),
    url(r'^profile/edit', 'speaker_edit', name='conference_speaker_edit'),
)
