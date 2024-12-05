from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get-guilds', views.get_guilds, name='get_guilds'),
    path('get-channels', views.get_channels, name='get_channels'),
    path('send-message', views.send_message, name='send-message'),
]