from datetime import datetime

from gatherings.conference.models import Event


def next_event(request):
    now = datetime.now()
    dec31 = datetime(now.year, 12, 31)
    next_event = Event.objects.get(start__gte=now, start__lte=dec31)
    return {'next_event': next_event}
