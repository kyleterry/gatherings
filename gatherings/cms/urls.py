from django.conf.urls import patterns, url

urlpatterns = patterns('gatherings.cms.views',
    url(r'^p/(?P<slug>[a-zA-Z0-9_.-]+)/$', 'view_page', name='cms_view_page'),
)
