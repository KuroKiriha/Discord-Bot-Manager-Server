import time, requests, json, asyncio, pytz, nextcord, aiohttp
from nextcord.ext import commands, application_checks
from nextcord import SlashOption, Interaction, Guild, ChannelType, activity
from nextcord.abc import GuildChannel
from datetime import datetime
from datetime import timedelta
from pytz import timezone
from bs4 import BeautifulSoup 

randomcat = ['http://random.cat/meow']

class fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name='cat', description='Send rendom cat picture.')
    async def randomcatpictre(self, bot: nextcord.Interaction):
        async with aiohttp.ClientSession() as session:
            async with session.get('http://aws.random.cat/meow') as r:
                if r.status == 200:
                    js = await r.json()
                    await bot.response.send_message(js['file'])
       
def setup(bot):
  bot.add_cog(fun(bot))