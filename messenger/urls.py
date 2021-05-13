from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('signup/', views.signup, name='signup'),
  path('channel/<str:title>/', views.channel_page, name='channel-page'),
  path('dialog/<str:username>/', views.dialog_page, name='dialog-page'),
]
