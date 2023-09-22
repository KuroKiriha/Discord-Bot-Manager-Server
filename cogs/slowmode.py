import time, requests, json, asyncio, pytz, nextcord
from nextcord.ext import commands, application_checks
from nextcord import SlashOption, Interaction, Guild, ChannelType, activity
from nextcord.abc import GuildChannel
from datetime import datetime
from datetime import timedelta
from pytz import timezone
from bs4 import BeautifulSoup

class slowmode(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @nextcord.slash_command(name="slowmode")
    @application_checks.has_permissions(administrator=True)
    async def slowmode(self, bot: Interaction):
       pass

    @slowmode.subcommand(description=f"Slow Mode type text channel.")
    @application_checks.has_permissions(administrator=True)
    async def textchannel(self, bot: Interaction, channel: nextcord.TextChannel, reason: str=SlashOption(description="Tell me why set this channel to slow mode.", required=True), hour: int=SlashOption(description="How many hour", required=False), min: int=SlashOption(description="How many minutes.", required=False), sec: int=SlashOption(description="How many seconds.",required=False)):
        try:
            #False
            if hour not in [1, 2, 6, None]:
                notify=nextcord.Embed(title="Error", description=f"[Hour] You can set delay slow mode to\n1 Hour\n2 Hour\n6 Hour\nOnly.")
                await bot.response.send_message(embed=notify, ephemeral=True)
            if min not in [1, 2, 5, 10, 15, 30, None]:
                notify=nextcord.Embed(title="Error", description=f"[Min] You can set delay slow mode to\n1 Min\n2 Min\n5 Min\n10 Min\n15 Min\n30 Min\nOnly.")
                await bot.response.send_message(embed=notify, ephemeral=True)
            if sec not in [0, 5, 10, 15, 30, None]:
                notify=nextcord.Embed(title="Error", description=f"[Min] You can set delay slow mode to\n0 Sec\n5 Sec\n10 Sec\n15 Sec\n30 Sec\nOnly.")
                await bot.response.send_message(embed=notify, ephemeral=True)
            #True
            if hour in [1, 2, 6]:
                if hour == 6:
                    second=21600
                    await channel.edit(slowmode_delay=second,reason=f"{bot.user} has set slow mode to {channel} to {hour} reason : {reason}")
                    await bot.response.send_message(f"{channel.mention} has set slow mode to {hour} H", delete_after=5)
                if hour == 2:
                    second=7200
                    await channel.edit(slowmode_delay=second,reason=f"{bot.user} has set slow mode to {channel} to {hour} reason : {reason}")
                    await bot.response.send_message(f"{channel.mention} has set slow mode to {hour} H", delete_after=5)
                if hour == 1:
                    second=3600
                    await channel.edit(slowmode_delay=second,reason=f"{bot.user} has set slow mode to {channel} to {hour} reason : {reason}")
                    await bot.response.send_message(f"{channel.mention} has set slow mode to {hour} H", delete_after=5)
            if min in [1, 2, 5, 10, 15, 30]:
                if min == 30:
                    second=1800
                    await channel.edit(slowmode_delay=second,reason=f"{bot.user} has set slow mode to {channel} to {min} reason : {reason}")
                    await bot.response.send_message(f"{channel.mention} has set slow mode to {min} M", delete_after=5)
                if min == 15:
                    second=900
                    await channel.edit(slowmode_delay=second,reason=f"{bot.user} has set slow mode to {channel} to {min} reason : {reason}")
                    await bot.response.send_message(f"{channel.mention} has set slow mode to {min} M", delete_after=5)
                if min == 10:
                    second=600
                    await channel.edit(slowmode_delay=second,reason=f"{bot.user} has set slow mode to {channel} to {min} reason : {reason}")
                    await bot.response.send_message(f"{channel.mention} has set slow mode to {min} M", delete_after=5)
                if min == 5:
                    second=300
                    await channel.edit(slowmode_delay=second,reason=f"{bot.user} has set slow mode to {channel} to {min} reason : {reason}")
                    await bot.response.send_message(f"{channel.mention} has set slow mode to {min} M", delete_after=5)
                if min == 2:
                    second=120
                    await channel.edit(slowmode_delay=second,reason=f"{bot.user} has set slow mode to {channel} to {min} reason : {reason}")
                    await bot.response.send_message(f"{channel.mention} has set slow mode to {min} M", delete_after=5)
                if min == 1:
                    second=60
                    await channel.edit(slowmode_delay=second,reason=f"{bot.user} has set slow mode to {channel} to {min} reason : {reason}")
                    await bot.response.send_message(f"{channel.mention} has set slow mode to {min} M", delete_after=5)
            if sec in [0, 5, 10, 15, 30]:
                if sec == 30:
                    second=30
                    await channel.edit(slowmode_delay=second,reason=f"{bot.user} has set slow mode to {channel} to {min} reason : {reason}")
                    await bot.response.send_message(f"{channel.mention} has set slow mode to {sec} S", delete_after=5)
                if sec == 15:
                    second=15
                    await channel.edit(slowmode_delay=second,reason=f"{bot.user} has set slow mode to {channel} to {min} reason : {reason}")
                    await bot.response.send_message(f"{channel.mention} has set slow mode to {sec} S", delete_after=5)
                if sec == 10:
                    second=10
                    await channel.edit(slowmode_delay=second,reason=f"{bot.user} has set slow mode to {channel} to {min} reason : {reason}")
                    await bot.response.send_message(f"{channel.mention} has set slow mode to {sec} S", delete_after=5)
                if sec == 5:
                    second=5
                    await channel.edit(slowmode_delay=second,reason=f"{bot.user} has set slow mode to {channel} to {min} reason : {reason}")
                    await bot.response.send_message(f"{channel.mention} has set slow mode to {sec} S", delete_after=5)
                if sec == 0:
                    second=0
                    await channel.edit(slowmode_delay=second,reason=f"{bot.user} has set slow mode to {channel} to {min} reason : {reason}")
                    await bot.response.send_message(f"{channel.mention} has set slow mode to {sec} S", delete_after=5)
        except:
            await bot.response.send_message(f"Something one is error.", ephemeral=True)

    @slowmode.subcommand(description=f"Turn off slow mode")
    @application_checks.has_permissions(administrator=True)
    async def textchannel_off(self, bot: Interaction, channel: nextcord.TextChannel):
        second=0
        await channel.edit(slowmode_delay=second)
        await bot.response.send_message(f"{channel.mention} slow mode is turn off.", delete_after=5)

def setup(bot):
  bot.add_cog(slowmode(bot))