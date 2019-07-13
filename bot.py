#!/usr/bin/env python3
# -- coding: utf-8 --
import logging
import os

from discord.ext import commands

# you need this line, and you forgot it
logging.basicConfig(level='INFO')


client = commands.Bot(command_prefix="=")


# do NOT use @client.event here, it breaks everything
@client.listen() 
async def on_message(message):
    nsfw_channel = client.get_channel(593050161467621395) 
    if message.channel == nsfw_channel and not message.attachments:
        await message.delete()


client.run(os.environ['TOKEN'])
