import time, requests, json, asyncio, pytz, nextcord
from nextcord.ext import commands, application_checks
from nextcord import SlashOption, Interaction, Guild, ChannelType, activity
from nextcord.abc import GuildChannel
from datetime import datetime
from datetime import timedelta
from pytz import timezone
from bs4 import BeautifulSoup

class serverinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name="server-info", description="See info your server.")
    async def serverinfo(self, bot: Interaction):
       ft = "%Y-%m-%d | %H:%M:%S | Time Zone : %Z | %z"
       ft2 = "%Y-%m-%d"
       tz = datetime.now(timezone('Asia/Bangkok'))
       member: nextcord.Member
       uif=nextcord.Embed(title=bot.guild, description='This is your server info', color=0x9efff9)
       uif.add_field(name='Name server', value=bot.guild)
       uif.add_field(name='ID server', value=bot.guild_id)
       uif.add_field(name='Verification server', value=bot.guild.verification_level)
       uif.add_field(name='Owner server', value=bot.guild.owner)
       uif.add_field(name='Owner ID server', value=bot.guild.owner_id)
       uif.add_field(name='Member', value=bot.guild.member_count)
       uif.add_field(name='Top roles', value=bot.guild.roles[-1])
       uif.add_field(name='Commands By', value=bot.user.mention)
       
       uif.timestamp = datetime.now(timezone('Asia/Bangkok'))
       uif.set_footer(text=tz.strftime(ft2))
       await bot.response.send_message(embed=uif)
       
    


def setup(bot):
  bot.add_cog(serverinfo(bot))