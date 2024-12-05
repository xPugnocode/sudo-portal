from django.shortcuts import render
from django.http import JsonResponse
from discordapp import bot
from asgiref.sync import async_to_sync
import asyncio

# Create your views here.
def index(request):
    return render(request, 'index.html')

def get_guilds(request):
    guilds = bot.get_all_guilds()
    return JsonResponse({'options' : guilds})

def get_channels(request):
    guild_id = int(request.GET.get('guild_id', None))
    channels = bot.get_all_channels(guild_id)
    return JsonResponse({'options' : channels})

def send_message(request):
    message = str(request.GET.get('message', None))
    channel_id = int(request.GET.get('channel_id', None))
    sync_send = asyncio.run_coroutine_threadsafe(bot.sudo_send(channel_id, message), bot.client.loop)
    result = sync_send.result()
    return JsonResponse({'result' : result})