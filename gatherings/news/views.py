from django.shortcuts import get_object_or_404
from annoying.decorators import render_to

from gatherings.news.models import Post, Tag


@render_to('news/list.html')
def list_all(request):
    news = Post.objects.published.order_by('-created_at')
    return locals()


@render_to('news/list.html')
def list_by_tag(request, tag):
    tag = get_object_or_404(Tag, slug=tag)
    news = Post.objects.published.filter(tags=tag).order_by('-created_at')
    return locals()


@render_to('news/view.html')
def view_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return locals()
