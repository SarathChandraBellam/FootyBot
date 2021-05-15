"""
Footybot
"""
# Generic Import
import sys
import logging
import random
# library import
import discord
from discord.ext import commands
from src.util import FOOTY_BOT_TOKEN, get_embed_from_file
from src.footy_commands import get_team_codes,get_league_standings

# initializing the Bot class (Sub class of Discord Client  
bot = commands.Bot(command_prefix='-')
bot.remove_command('help!')
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
            help_embed = get_embed_from_file("help_embed.json")
            await channel.send('Hey There! I am Footybot. I Just got added to this channel!', embed=help_embed)
            break


@bot.event
async def on_member_join(member):
    await member.send(f"Hi , welcome to the Server")


@bot.command(name='cc', help="Respond with competitions code", alias=["lc", "league_codes", "competition_codes"])
async def competitions_codes(message):
    comp_code_embed = get_embed_from_file('competitions_embed.json')
    comp_code_embed.set_footer(text='Requested By: ' + str(message.author))
    await message.send(embed=comp_code_embed)


@bot.command(name='help', help="Respond with all available commands", alias=["h", "help!"])
async def help(message):
    comp_code_embed = get_embed_from_file('help_embed.json')
    comp_code_embed.set_footer(text='Requested By: ' + str(message.author))
    await message.send(embed=comp_code_embed)


@bot.command(name='tc', help="Respond with league wise team codes", alias=["team_codes"])
async def team_codes(message, league_code=None ):
    print(league_code)
    team_code_embed = get_team_codes(league_code)
    team_code_embed.set_footer(text='Requested By: ' + str(message.author))
    await message.send(embed=team_code_embed)


@bot.command(name='standings', help="League table and standings", alias=["s"])
async def standings(message, league_code=None ):
    if league_code is not None:
        league_stands = get_league_standings(league_code)
        if league_stands is not None:
            await message.send(league_stands)
        else:
            await message.send(embed=discord.Embed(title=f" Team codes of League - {league_code}",
                                                   description=f"League code {league_code} is invalid"))
    else:
        await message.send(embed=discord.Embed(ttitle=f" Team codes of League - {league_code}",
                                                   description="No league code provided"))



@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    response = message.content.lower()
    if response.startswith(("foot", "bot")):
        await message.channel.send(f"Hi {message.author}", embed=get_embed_from_file("help_embed.json"))
    elif response.startswith("good"):
        day_quotes = ["Wishing you a great day..",
                      "May you be loved more and more today..",
                      "Enjoy the great day you are blessed with",
                      "Have a great day! This is my wish for you today",
                      "New day comes with new hopes and new opportunities"]
        resp = random.choice(day_quotes)
        await message.channel.send(resp)
    elif response.startswith("love"):
        love_quotes = ["Love is the most beautiful thing in this world, \
                      it cannot be seen or even heard but must be felt with the heart.",
                       "Life without love is like a tree without blossoms or fruit",
                       "Love recognizes no barriers. It jumps hurdles, leaps fences, \
                      penetrates walls to arrive at its destination full of hope.",
                      ]

        resp = random.choice(love_quotes)
        await message.channel.send(resp)
    # on_message() and @bot.command issue doesn't work together unless you add the below command
    # Overriding the default provided on_message forbids any extra commands from running.
    # To fix this, add a bot.process_commands(message) line at the end of your on_message.
    await bot.process_commands(message)


bot.run(FOOTY_BOT_TOKEN)
