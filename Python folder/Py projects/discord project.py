import  discord 
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event

async def on_ready():
    print("bot is ready.")
    
    
client.run('ODM1NjQzMzk3NDk0MDE0MDAz.YISbjw.7k_WEVufXIMi_U_9U2vjgpNOex8') #token 

