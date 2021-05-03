import discord
import logging
import sys
from discord.ext import commands

#decorator
client = commands.Bot(command_prefix = '.')


# LOGGING FORMAT
logger = logging.getLogger()
LEVELS = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'critical': logging.CRITICAL
}
default_level = LEVELS['debug']
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



@client.event
async def on_ready():
    print("Bot is ready!")

@client.event
async def on_member_join(member):
    print(f'{member} has joined a server.')

@client.event
async def on_member_remove(member):
    print(f'{member} has left a server.')

@client.command(aliases=['Germany','Bundesliga'])
async def bliga(ctx):
    await ctx.send('Hallo!')


#add token here
client.run('')