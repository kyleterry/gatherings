from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from annoying.decorators import render_to

from gatherings.cms.models import Page


@render_to('cms/view_page.html')
def view_page(request, slug):
    page = Page.objects.get(slug=slug)
    if page.slug == 'home-page':
        return HttpResponseRedirect(reverse('home'))
    return locals()
