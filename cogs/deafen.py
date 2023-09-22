import time, requests, json, asyncio, pytz, nextcord
from nextcord.ext import commands, application_checks
from nextcord import SlashOption, Interaction, Guild, ChannelType, activity
from nextcord.abc import GuildChannel
from datetime import datetime
from datetime import timedelta
from pytz import timezone
from bs4 import BeautifulSoup

class deafen(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.start_time = time.time()

    @nextcord.slash_command(name="deafen",description=f"Do you want to move someone?")
    @application_checks.has_permissions(administrator=True)
    async def deafen(self, bot: nextcord.Interaction, user: nextcord.User, reason: str=SlashOption(description='Tell me your reason why move that user', required=False)):
        try:
            await user.edit(deafen=True)
            await bot.response.send_message(f"Member {user.mention} has been deafend :D", delete_after=5)
        except:
            await bot.response.send_message(f"I can't deafen {user} sad", delete_after=5)


def setup(bot):
  bot.add_cog(deafen(bot))