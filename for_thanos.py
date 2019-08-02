#!/usr/bin/env python3
# -- coding: utf-8 --
import logging
import os
import discord
from discord.ext import commands
from discord.utils import get

# you need this line, and you forgot it
logging.basicConfig(level='INFO')

client = commands.Bot(command_prefix="=", case_insensitive=True)

# do NOT use @client.event here, it breaks everything
@client.listen() 
async def on_message(message):
    nsfw_channel = client.get_channel(593050161467621395) 
    general = client.get_channel(586147813730025503) 
    if message.channel == nsfw_channel and not message.attachments:
        await message.delete()
    elif message.channel == general and message.attachments:
        await message.delete()

#ngl I've never used a command system like this before so I'm kind of going improv

@client.command(pass_context=True) # this makes sure the ctx var is there 
@commands.has_role("Admin")
async def mute(ctx, user: discord.Member):
 client.add_roles(user, get(ctx.guild, "Muted")) # change "Muted"
 await ctx.send('{0} has been muted!'.format(user))
  # I think this should work but honestly I have no idea
	
  

client.run(os.environ['TOKEN'])
