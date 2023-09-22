import time, requests, json, asyncio, pytz, nextcord
from nextcord.ext import commands, application_checks
from nextcord import SlashOption, Interaction, Guild, ChannelType, activity
from nextcord.abc import GuildChannel
from datetime import datetime
from datetime import timedelta
from pytz import timezone
from bs4 import BeautifulSoup



api_key = "c12382c2792d3efaa04e144973438ec2"
base_url = "http://api.openweathermap.org/data/2.5/weather?"

class weathercheck(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @nextcord.slash_command(description="🌡️ - It sends information about the selected location temperature.")
    async def weathernow(self, bot: nextcord.Interaction, city: str):
        city_name=city
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name
        response = requests.get(complete_url)
        x=response.json()
        channel = bot.channel
        if x["cod"] != "404":
	        async with channel.typing():
                    y = x["main"]
                    current_temperature = y["temp"]
                    current_temperature_celsiuis = str(round(current_temperature - 273.15))
                    current_pressure = y["pressure"]
                    current_humidity = y["humidity"]
                    z = x["weather"]
                    weather_description = z[0]["description"]
                    weather_description = z[0]["description"]
                    embed = nextcord.Embed(title=f"Weather in {city_name}")
                    embed.add_field(name="Descripition", value=f"**{weather_description}**", inline=False)
                    embed.add_field(name="Temperature(C)", value=f"**{current_temperature_celsiuis}°C**", inline=False)
                    embed.add_field(name="Humidity(%)", value=f"**{current_humidity}%**", inline=False)
                    embed.add_field(name="Atmospheric Pressure(hPa)", value=f"**{current_pressure}hPa**", inline=False)
                    embed.set_thumbnail(url="https://i.ibb.co/CMrsxdX/weather.png")
                    embed.set_footer(text=f"Requested by {bot.user.mention}")
                    await bot.response.send_message(embed=embed, ephemeral=True)
        else:
        	await bot.response.send_message("City not found.", ephemeral=True)



def setup(bot):
  bot.add_cog(weathercheck(bot))