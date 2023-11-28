
import discord
import discord.ext

intents = discord.Intents.all() 
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("ready")


client.run()