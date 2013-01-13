from django.contrib import admin

from gatherings.news.models import Post, Tag


admin.site.register(Post)
admin.site.register(Tag)
