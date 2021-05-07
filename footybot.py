import os
import discord
from discord.utils import find
from dotenv import load_dotenv


load_dotenv()

FOOTY_BOT_TOKEN = os.getenv("FOOTY_BOT_TOKEN")
API_TOKEN = os.getenv("API_TOKEN")
API_ORG = os.getenv("API_ORG")

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord')


@client.event
async def on_guild_join(guild):
    """
    Asynchronous method to send a message from bot whenever it join a new guild/server
    :param guild: Guild Instance
    :return: None, Sends a message to the general channel
    """
    general = find(lambda x: x.name == 'general',  guild.text_channels)
    if general and general.permissions_for(guild.me).send_messages:
        await general.send('Hello {}!'.format(guild.name))


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f"Hi {member.name}, Welcome to Discord Server")


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    response = message.content.lower()
    if response.startswith("hi"):
        await message.channel.send(f"Hi {message.author}, Love You 3000")

client.run(FOOTY_BOT_TOKEN)
