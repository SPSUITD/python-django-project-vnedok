from django import forms

from .models import ChannelMessage, PrivateMessage


class ChannelMessageForm(forms.ModelForm):
  class Meta:
    model = ChannelMessage
    fields = ('body',)


class PrivateMessageForm(forms.ModelForm):
  class Meta:
    model = PrivateMessage
    fields = ('body',)