import time, requests, json, asyncio, pytz, nextcord
from nextcord.ext import commands, application_checks
from nextcord import SlashOption, Interaction, Guild, ChannelType, activity
from nextcord.abc import GuildChannel
from datetime import datetime
from datetime import timedelta
from pytz import timezone
from bs4 import BeautifulSoup

class kick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
      
    @commands.Cog.listener()
    async def on_message(self, message):
        print(message)

    @nextcord.slash_command(name='kick', description='Kick some member in your guild.') #Work
    @application_checks.has_permissions(administrator=True)
    async def kick(self, bot: nextcord.Interaction, member: nextcord.Member=SlashOption(description="Select a member"), reason: str=SlashOption(description='Tell me your reason why kick', required=False)):
        if reason == None:
            reason = f"No reason by {bot.user}"
            em = nextcord.Embed(title=f'{member.mention}',description=f'{member.mention} has been kicked out of guild.', color=0xff0000)
            em.add_field(name=f'Reason', value=f'{reason}')
            em.timestamp = datetime.now()
            await bot.response.send_message(embed=em, ephemeral=True)
            dm = nextcord.Embed(title='Your has been kicked from server', description=f'{member.mention} you has been kicked from __**{bot.guild}**__', color=0xff0000)
            dm.add_field(name=f'Reason', value=f'{reason}')
            dm.add_field(name='Info', value=f'Guild name : {bot.guild}\n Guild ID : {bot.guild_id}')
            await member.send(embed=dm)
            await member.guild.kick(member, reason=reason)
        else:
            em = nextcord.Embed(title=f'{member.mention}',description=f'{member.mention} has been kicked out of guild.', color=0xff0000)
            em.add_field(name=f'Reason', value=f'{reason}')
            em.timestamp = datetime.now()
            await bot.response.send_message(embed=em, ephemeral=True)
            dm = nextcord.Embed(title='Your has been kicked from server', description=f'{member.mention} you has been kicked from __**{bot.guild}**__', color=0xff0000)
            dm.add_field(name=f'Reason', value=f'{reason}')
            dm.add_field(name='Info', value=f'Guild name : {bot.guild}\n Guild ID : {bot.guild_id}')
            await member.send(embed=dm)
            await member.guild.kick(member, reason=f'{reason} kick by : {bot.user}')

def setup(bot):
  bot.add_cog(kick(bot))