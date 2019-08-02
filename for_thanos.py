#!/usr/bin/env python3
# -- coding: utf-8 --
import logging
import os
import requests
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


@client.command() 
@commands.has_any_role("Admin", "Mod", "Chat Mod")
async def mute(ctx, user: discord.Member):
    await user.add_roles(discord.utils.get(ctx.guild.roles, name = "Muted"))
    await ctx.send('{0} has been muted!'.format(user))
    await ctx.message.delete()
	
 
@client.command() 
@commands.has_any_role("Admin", "Mod", "Chat Mod")
async def unmute(ctx, user: discord.Member):
    await user.remove_roles(discord.utils.get(ctx.guild.roles, name = "Muted"))
    await ctx.send('{0} has been  unmuted!'.format(user))
    await ctx.message.delete()


@client.command()
async def jointheforce(ctx):
    user = ctx.message.author 
    await user.add_roles(discord.utils.get(ctx.guild.roles, name = "Thanos' Children"))
    embed = discord.Embed(title = "welcome {0} to the family!".format(ctx.message.author.name))
    embed.set_image(url ="https://static.comicvine.com/uploads/original/11113/111131285/6475508-9502292318-64162.gif ")
    await ctx.send("You are now my child...", embed = embed)
    await ctx.message.delete()
	
	
@client.command()
async def leavetheforce(ctx):
    user = ctx.message.author 
    await user.remove_roles(discord.utils.get(ctx.guild.roles, name = "Thanos' Children"))
    embed = discord.Embed(title = "Farewell {0} to the family... You are on your own now...".format(ctx.message.author.name))
    embed.set_image(url ="https://i1.wp.com/78.media.tumblr.com/b4171532756933ce3014e9ddffe0fbce/tumblr_pcp1aiorRo1sc0ffqo5_540.gif?w=605&ssl=1 ")
    await ctx.send(f"You have failed me... {ctx.message.author.mention} left the family...", embed = embed)
    await ctx.message.delete()


client.run(os.environ['TOKEN'])

