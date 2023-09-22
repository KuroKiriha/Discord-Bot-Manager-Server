import time, requests, json, asyncio, pytz, nextcord
from nextcord.ext import commands, application_checks
from nextcord import SlashOption, Interaction, Guild, ChannelType, activity
from nextcord.abc import GuildChannel
from datetime import datetime
from datetime import timedelta
from pytz import timezone
from bs4 import BeautifulSoup


    

class ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name='ban', description='Ban some member in your guild.')
    @application_checks.has_permissions(administrator=True)
    async def ban(self, bot: nextcord.Interaction, member: nextcord.Member=SlashOption(description='Select a member'), reason: str=SlashOption(description='Tell me your reason why ban.', required=True), delete_message_days=SlashOption(description='How many day to delete message (max 7 day)', required=False) ):
        if reason == None:
            await bot.response.send_message(f"Sorry i can't ban this user because no reason to ban.")
            return
        else:
            em = nextcord.Embed(title=f'{member}',description=f'{member} has been baned out of guild.', color=0xff0000)
            em.add_field(name=f'Reason', value=f'{reason}')
            em.timestamp = datetime.now()
            await bot.response.send_message(embed=em, ephemeral=True)
            dm = nextcord.Embed(title='Your has been baned from server', description=f'{member} you has been baned from __**{bot.guild}**__', color=0xff0000)
            dm.add_field(name=f'Reason', value=f'{reason}')
            dm.add_field(name='Info', value=f'Guild name : {bot.guild}\n Guild ID : {bot.guild_id}')
            await member.send(embed=dm)
            await member.guild.ban(member, reason=f'{reason} kick by : {bot.user}')

def setup(bot):
  bot.add_cog(ban(bot))