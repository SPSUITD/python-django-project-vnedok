from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model, forms
from django.db.models import Q

from .models import Channel, PrivateMessage, ChannelMessage
from .forms import ChannelMessageForm, PrivateMessageForm


User = get_user_model()


def index(request):
  channels = Channel.objects.all()
  users = User.objects.exclude(pk=request.user.pk)
  return render(request, 'index.html',
               {'channels': channels, 'users': users})


def channel_page(request, title):
  channel = get_object_or_404(Channel, title=title)
  if request.method == 'POST':
    form = ChannelMessageForm(request.POST)
    if form.is_valid():
      message = form.save(commit=False)
      message.channel = channel
      message.author = request.user
      message.save()
    return redirect('channel-page', title=channel.title)

  messages = ChannelMessage.objects.filter(
    channel=channel
  ).order_by('publication_time')
  return render(request, 'channel.html', {'messages': messages})


def dialog_page(request, username):
  user = get_object_or_404(User, username=username)
  if request.method == 'POST':
    form = PrivateMessageForm(request.POST)
    if form.is_valid():
      message = form.save(commit=False)
      message.user_from = request.user
      message.user_to = user
      message.save()
    return redirect('dialog-page', username=username)
  
  messages = PrivateMessage.objects.filter(
    Q(user_from=request.user,user_to=user) |
    Q(user_from=user,user_to=request.user)  
  ).order_by('publication_time')
  return render(request, 'dialog.html', {'messages': messages})

def signup(request):
    if request.method == 'POST':
        form = forms.UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = forms.UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})