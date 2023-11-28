
import discord
import discord.ext

intents = discord.Intents.all() 
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("ready")


client.run("MTE3NzkzNzY3ODQxMTUwMTU5OA.G3CZJ0.LNbpVzjfRU5nAFlLBinuST4TOFPahye2pYf7aM")