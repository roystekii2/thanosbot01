import discord
from discord.ext import commands 
client = commands.Bot(command_prefix = "=")

@client.event
async def on_message(message):
    nsfw_ch = client.get_channel(593050161467621395)
    if message.channel == nsfw_ch:
        if not message.attachments:
            message.delete()


client.run(process.env."NTk3Nzc5NTkzODkzNjQyMjQw.XSNDtA.ty_tS837tt6sLM3aqXVr85QmUyA")
