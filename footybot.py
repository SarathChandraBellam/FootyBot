"""
Footybot
"""
import os
import discord
import logging
import sys
from discord.utils import find
from discord.ext import commands
from src.util import FOOTY_BOT_TOKEN

# initializing the Bot class (Sub class of Discord Client  
bot = commands.Bot(command_prefix='$')
bot.remove_command('help')

# LOGGING FORMAT
logger = logging.getLogger()
LEVELS = {
    'debug': logging.DEBUG,
    'info': logging.INFO,
    'warning': logging.WARNING,
    'error': logging.ERROR,
    'critical': logging.CRITICAL
}
default_level = LEVELS['info']
log_message = '%(asctime)s:%(levelname)s FileName:%(filename)s LineNo:%(lineno)d  Message:%(message)s'
if not len(logger.handlers):
    logger.setLevel(default_level)
    # create formatter
    formatter = logging.Formatter(log_message)
    # create console handler and set level to debug
    stream = logging.StreamHandler(sys.stdout)
    stream.setLevel(default_level)
    stream.setFormatter(logging.Formatter(log_message))
    logger.addHandler(stream)


@bot.event
async def on_ready():
    """
    Changing the presence of the client
    """
    print(f'{bot.user} has connected to Discord')
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.listening,
            name=".help on " + str(len(bot.guilds)) + " server(s)")
    )


@bot.event
async def on_guild_join(guild):
    """
    Asynchronous method to send a message from bot whenever it join a new guild/server
    :param guild: Guild Instance
    :return: None, Sends a message to the general channel
    """
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            help_embed = footy_commands.getHelpEmbed()
            await channel.send('Hey There! I am Footybot. I Just got added to this channel!\
                \nBasic commands are listed below :)', embed=help_embed)
            break


@bot.event
async def on_member_join(member):
    await member.send(f"Hi , welcome to the Server")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    response = message.content.lower()
    if response.startswith("hi"):
        await message.channel.send(f"Hi {message.author}, Love You 3000")


@bot.command(name='99', help='Responds with a random quote from Brooklyn 99')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        'Cool. Cool cool cool cool cool cool cool,\
        \nno doubt no doubt no doubt no doubt.',
        'If I die, turn my tweets into a book',
        'Captain Wuntch. Good to see you. But if you’re here, who’s guarding Hades?',
        'Anyone over the age of six celebrating a birthday should go to hell.'
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)


bot.run(FOOTY_BOT_TOKEN)
