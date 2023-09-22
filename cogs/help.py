import time, requests, json, asyncio, pytz, nextcord, threading, re
from nextcord.ext import commands, application_checks
from nextcord import SlashOption, Interaction, Guild, ChannelType, activity, VoiceProtocol, voice_client
from nextcord.abc import GuildChannel   
from spotipy.oauth2 import SpotifyOAuth
from datetime import datetime
from datetime import timedelta
from pytz import timezone
from bs4 import BeautifulSoup
from threading import Thread

class ButtonClass(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.value = [None]

    @nextcord.ui.button(label="1", style=nextcord.ButtonStyle.blurple)
    async def button1(self, button: nextcord.ui.Button, interaction: nextcord.Interaction, custom_id="button:1"):
        self.value = [interaction.user, 1]
        await interaction.response.send_message("You pressed 1!", ephemeral=True)
        # Reset the view after handling the interaction
        self.reset_view()

    @nextcord.ui.button(label="2", style=nextcord.ButtonStyle.blurple, custom_id="button:2")
    async def button2(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        self.value = [interaction.user, 2]
        await interaction.response.send_message("You pressed 2!", ephemeral=True)
        # Reset the view after handling the interaction
        self.reset_view()

    def reset_view(self):
        self.value = [None]
        for child in self.children:
            child.disabled = False

class TestingCommand(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.persistent_views_added = False

    @commands.command(help="Cooldown test command")
    async def test(self, ctx, msg=""):
        view = ButtonClass()
        test = await ctx.send("Press a button:", view=view)



def setup(client):
    client.add_cog(TestingCommand(client))
