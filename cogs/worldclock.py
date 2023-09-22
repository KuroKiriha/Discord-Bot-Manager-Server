import time, requests, json, asyncio, pytz, nextcord
from nextcord.ext import commands, application_checks
from nextcord import SlashOption, Interaction, Guild, ChannelType, activity
from nextcord.abc import GuildChannel
from datetime import datetime
from datetime import timedelta
from pytz import timezone
from bs4 import BeautifulSoup

class wc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name="time-world", description="Show Local time now.")
    async def WC(self, bot: nextcord.Interaction):
        time_zones = pytz.all_timezones
        embedtime = nextcord.Embed(title="Current Time in Time Zones Around the World", color=0x00ff00)
        for tz_name in time_zones:
            tz = pytz.timezone(tz_name)
            CT =datetime.now(tz)
            embedtime.add_field(name=tz_name, value=CT.strftime("%Y-%m-%d %H:%M:%S"), inline=True)
        await bot.response.send_message(embed=embedtime)

def setup(bot):
  bot.add_cog(wc(bot))