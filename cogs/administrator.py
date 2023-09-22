import time, requests, json, asyncio, pytz, nextcord
from nextcord.ext import commands, application_checks
from nextcord import SlashOption, Interaction, Guild, ChannelType, activity
from nextcord.abc import GuildChannel
from datetime import datetime
from datetime import timedelta
from pytz import timezone
from bs4 import BeautifulSoup

class administrator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name="clear", description="Clears messages")
    @application_checks.has_guild_permissions(administrator=True)
    async def clear(self, interaction: nextcord.Interaction, amount: int = SlashOption(name="amount", description="Enter the amount of the messages.")):
        if amount > 1000:
            await interaction.response.send_message('Cannot delete more than 1000 messages.', ephemeral=True)
        else:
            await interaction.channel.purge(limit=amount)  # type: ignore
            await interaction.response.send_message(f"Successfully cleared {amount} messages", ephemeral=True)
    
    @nextcord.slash_command(name='create-embed',description='Create a custom embed.')
    @application_checks.has_permissions(administrator=True)
    async def create_mbed(self, bot: nextcord.Interaction, title: str, description: str, url=None, ):
        em = nextcord.Embed(title=title, description=description, url=url, color=0x00ffbf)
        em.set_author(name=bot.user)
        em.timestamp = datetime.now()
        await bot.response.send_message(embed=em)

    @nextcord.slash_command(name='hellocommand', description='test commands in cogs')
    async def hellocommand(self, bot: nextcord.Interaction):
        await bot.response.send_message('Test commands in cogs is working!')
        

def setup(bot):
  bot.add_cog(administrator(bot))