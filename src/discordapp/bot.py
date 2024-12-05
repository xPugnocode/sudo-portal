import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
import asyncio

load_dotenv()

client = commands.Bot(command_prefix='$', intents=discord.Intents.all())

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Game('dead... temporarily.'))
    print('Initilization done.')

@client.tree.command(name="ping", description="get the latency")
async def ping(interaction):
    await interaction.response.send_message(f"Ping: {client.latency*1000}ms")


@client.command()
async def sync(ctx):
    print("sync command")
    if ctx.author.id == 567924760370085899:
        await client.tree.sync()
        await ctx.send('Command tree synced.')

def get_all_guilds():
    try:
        return [{'value' : str(guild.id), 'text' : guild.name} for guild in client.guilds]
    except:
        return None

def get_all_channels(guild_id):
    # try:
        guild = client.get_guild(guild_id)
        channels = guild.text_channels
        if guild != None:
            return [{'value' : str(channel.id), 'text' : channel.name} for channel in channels]
        else:
            print('we fricked up1')
            return None
    # except Exception as e:
    #     print('we fricked up', e)
    #     return None

async def sudo_send(channel_id, message):
    try:
        channel = client.get_channel(channel_id)
        await channel.send(message)
        return True
    except Exception as e:
        print(e)
        return False

def runBot():
    client.run(os.getenv("TOKEN"))

if __name__ == "__main__":
    try:
        client.run(os.getenv("TOKEN"))
    except discord.HTTPException as e:
        if e.status == 429:
            print(
                "The Discord servers denied the connection for making too many requests"
            )
            print(
                "Get help from https://stackoverflow.com/questions/66724687/in-discord-py-how-to-solve-the-error-for-toomanyrequests"
            )
        else:
            raise e
