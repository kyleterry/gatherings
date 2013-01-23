from gatherings.news.models import Post


def latest_news(request):
    news = Post.objects.published.order_by('-created_at')[:10]
    return locals()
