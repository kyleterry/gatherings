from django import forms

from gatherings.conference.models import Speaker


class SpeakerForm(forms.ModelForm):

    class Meta:
        model = Speaker
        fields = ('bio', 'image')
