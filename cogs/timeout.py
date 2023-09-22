import time, requests, json, asyncio, pytz, nextcord
from nextcord.ext import commands, application_checks
from nextcord import SlashOption, Interaction, Guild, ChannelType, activity
from nextcord.abc import GuildChannel
from datetime import datetime
from datetime import timedelta
from pytz import timezone
from bs4 import BeautifulSoup

class timeout(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
            
    @nextcord.slash_command(name='timeout', description='Soft ban with timeout.')
    async def timeout(self, bot: nextcord.Interaction, member:nextcord.Member, reason: str=SlashOption(description='Tell me your reason why timeout', required=True), days: int=SlashOption(description='How many days', required=False), hour: int=SlashOption(description='How many hour(s)', required=False), min: int=SlashOption(description='How many minutes', required=False), sec: int=SlashOption(description='How many seconds', required=False)):
        if days == None:
            days=0
        if hour == None:
            hour=0
        if min == None:
            min=0
        if sec == None:
            sec=0
        timeoutdelta = timedelta(days=days, hours=hour, minutes=min, seconds=sec)
        if reason == None:
            await bot.response.send_message(f"Sorry i can't timeout this user because no reason to timeout.")
            return
        else:
            await member.edit(timeout=timeoutdelta)
            await bot.response.send_message(f'User {member.mention} has been timeout for {days} day {hour} Hour {min} min and {sec} sec.', ephemeral=True)

    @nextcord.slash_command(name='stop-timeout', description='Stop timeout.')
    async def stoptimeout(self, bot: nextcord.Interaction, member:nextcord.Member, reason: str=SlashOption(description='Tell me your reason why timeout', required=True)):
        days=0
        hour=0
        min=0
        sec=0
        timeoutdelta = timedelta(days=days, hours=hour, minutes=min, seconds=sec)
        await member.edit(timeout=timeoutdelta)
        await bot.response.send_message(f'User {member.mention} has been stop timeout', ephemeral=True)

def setup(bot):
  bot.add_cog(timeout(bot))