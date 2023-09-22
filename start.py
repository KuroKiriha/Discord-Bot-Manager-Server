import nextcord, os ,datetime, time, asyncio, config, pytz, random, flask, lavalink
from nextcord.ext import commands, tasks
from stroage import badwordlist
from datetime import datetime
from random import choice, choices

starttime = time.time() # snapshot of time when listener sends on_ready
global startTime #global variable to be used later in cog

Intents = nextcord.Intents().all()
bot = commands.Bot(command_prefix='km!', intents=Intents)

@bot.event
async def on_ready():
    Thaizonetime = pytz.timezone("Asia/Bangkok")
    ft="%H:%M:%S"
    timenow = datetime.now(Thaizonetime).strftime(ft)
    change_status.start()
    print("\n| ----------------- |")
    print(f'\n[INFO] {timenow} Now my name is {bot.user.name} is ready')
    print(f"[INFO] {timenow} My full name is {bot.user} | My ID is {bot.user.id} | My discrim is {bot.user.discriminator}")
    print(f"[INFO] {timenow} My owner is Kuro Kiriha#6690")
    print(f"\n[Start] {timenow} Start task loop Activity !")
    print(f"[Start] {timenow} Start Flask server. !")
    print(f"[Start] {timenow} Start lavalink(Mafic) node. !")
    print("\n| ----------------- |\n")
    print(f"Stand by . . . \n")


countload=0
print("\n| ----------------- |\n")
for filename in os.listdir('./cogs'):
    Thaizonetime = pytz.timezone("Asia/Bangkok")
    ft="%H:%M:%S"
    timenow = datetime.now(Thaizonetime).strftime(ft)
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')
        print(f"[INFO] {timenow} {filename} is loaded")
        countload+=1
print(f"\nAll file(s) {countload} is loaded and ready to use ! ! !")

def convert_timedelta(duration): # Function to convert the time
    days, seconds = duration.days, duration.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = (seconds % 60)
    return days, hours, minutes, seconds

@bot.slash_command(description="My first slash command")
async def hello(interaction: nextcord.Interaction):
    await interaction.response.send_message("Hello!", ephemeral=True)

namesteam = ["Watching Kiriha", "Playing with cat", "Steaming with Kiriha", "Playing with Kiriha", "Love Kiriha", "Kuro is the best"]

@tasks.loop(seconds=30)
async def change_status():
    await bot.change_presence(activity=nextcord.Streaming(name=f"{choice(namesteam)}", url="https://www.twitch.tv/kurokiriha"))

bot.run(config.TOKEN)