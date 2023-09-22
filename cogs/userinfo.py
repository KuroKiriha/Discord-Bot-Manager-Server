import time, requests, json, asyncio, pytz, nextcord
from nextcord.ext import commands, application_checks
from nextcord import SlashOption, Interaction, Guild, ChannelType, activity
from nextcord.abc import GuildChannel
from datetime import datetime
from datetime import timedelta
from pytz import timezone
from bs4 import BeautifulSoup



class userinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name="user-info", description="See info your server.")
    async def userinfo(self, bot: Interaction, member: nextcord.Member):
        ft = "%Y-%m-%d | %H:%M:%S | Time Zone : %Z | %z"
        ft2 = "%Y-%m-%d"
        ft3 = "%Y-%m-%d | %H:%M:%S | Time Zone : %Z"
       
        memberAvatar = member.avatar.url
       
        if memberAvatar == None:
            sif=nextcord.Embed(title=member, description=f'{member} info', color=0x9efff9)
            sif.add_field(name='User (mention)', value=member.mention)
            sif.add_field(name='User ', value=member)
            sif.add_field(name='Tag', value=member.discriminator)
            sif.add_field(name='User ID', value=member.id)
            sif.add_field(name='User joined', value=member.joined_at.strftime(ft2))
            sif.add_field(name='Account age', value=member.created_at.strftime(ft3))
            sif.set_author(name=member, icon_url="https://media.istockphoto.com/id/1322277517/photo/wild-grass-in-the-mountains-at-sunset.jpg?s=612x612&w=0&k=20&c=6mItwwFFGqKNKEAzv0mv6TaxhLN3zSE43bWmFN--J5w=")
            sif.set_thumbnail(url="https://media.istockphoto.com/id/1322277517/photo/wild-grass-in-the-mountains-at-sunset.jpg?s=612x612&w=0&k=20&c=6mItwwFFGqKNKEAzv0mv6TaxhLN3zSE43bWmFN--J5w=")
            tz = datetime.now(timezone('Asia/Bangkok'))
            sif.timestamp = datetime.now(timezone('Asia/Bangkok'))
            sif.set_footer(text=tz.strftime(ft2))
            await bot.response.send_message(embed=sif)
        else:
            sif=nextcord.Embed(title=member, description=f'{member} info', color=0x9efff9)
            sif.add_field(name='User (mention)', value=member.mention)
            sif.add_field(name='User ', value=member)
            sif.add_field(name='Tag', value=member.discriminator)
            sif.add_field(name='User ID', value=member.id)
            sif.add_field(name='User joined', value=member.joined_at.strftime(ft2))
            sif.add_field(name='Account age', value=member.created_at.strftime(ft3))
            sif.set_author(name=member, icon_url=memberAvatar)
            sif.set_thumbnail(url=memberAvatar)
            tz = datetime.now(timezone('Asia/Bangkok'))
            sif.timestamp = datetime.now(timezone('Asia/Bangkok'))
            sif.set_footer(text=tz.strftime(ft2))
            await bot.response.send_message(embed=sif)
    
    @nextcord.slash_command(name='avatar', description='See avater user')
    async def avatar(self, bot: nextcord.Interaction, member: nextcord.Member):
        ft = "%Y-%m-%d | %H:%M:%S | Time Zone : %Z | %z"
        ft2 = "%Y-%m-%d"
        ft3 = "%Y-%m-%d | %H:%M:%S | Time Zone : %Z"
        avt=nextcord.Embed(title=member, description=f'Look this is avatar of {member}. ♥♥')
        memberAvatar = member.avatar.url
        avt.set_image(url=memberAvatar)
        tz = datetime.now(timezone('Asia/Bangkok'))
        avt.timestamp = datetime.now(timezone('Asia/Bangkok'))
        avt.set_footer(text=tz.strftime(ft2))
        await bot.response.send_message(embed=avt)


def setup(bot):
  bot.add_cog(userinfo(bot))