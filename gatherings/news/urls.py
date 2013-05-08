from django.conf.urls import patterns, url

urlpatterns = patterns('gatherings.news.views',
    url(r'^news/by-tag/(?P<tag>[-\w]+)/$', 'list_by_tag', name='news_list_by_tag'),
    url(r'^news/(?P<post_id>\d)/', 'view_post', name='news_view_post'),
    url(r'^news/$', 'list_all', name='news_list'),
)
