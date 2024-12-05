from django.apps import AppConfig
from threading import Thread
from . import bot
import os

started = False

class DiscordappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'discordapp'

    def ready(self):
        if not started:
            thread = Thread(target=bot.runBot, args=[])
            thread.start()