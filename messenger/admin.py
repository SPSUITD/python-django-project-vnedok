from django.contrib import admin

from .models import PrivateMessage, Channel, ChannelMessage

admin.site.register(PrivateMessage)
admin.site.register(Channel)
admin.site.register(ChannelMessage)
