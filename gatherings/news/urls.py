from django.conf.urls import patterns, url

urlpatterns = patterns('gatherings.news.views',
    url(r'^news/(?P<post_id>\d)/', 'view_post', name='news_view_post'),
)
