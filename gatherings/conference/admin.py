from django.contrib import admin

from gatherings.conference.models import (Event, Session, Speaker, Room, Track)


admin.site.register(Event)
admin.site.register(Session)
admin.site.register(Speaker)
admin.site.register(Room)
admin.site.register(Track)
