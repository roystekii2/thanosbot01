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

	
@client.command()
async def snap(ctx):
    user = ctx.message.author 
    embed = discord.Embed(title = "OH SNAP!".format(ctx.message.author.name))
    embed.set_image(url ="https://media1.tenor.com/images/e36fb32cfc3b63075adf0f1843fdc43a/tenor.gif?itemid=12502580 ")
    await ctx.send(f"I can do it with a snap of fingers, and you all cease to exist ", embed = embed)
    await ctx.message.delete()

@client.command()
async def thanoschildren(ctx):
    await ctx.send(f"current server members: {ctx.guild.member_count}")
    await ctx.message.delete()


@client.command()
async def thanosdance(ctx):
    user = ctx.message.author 
    embed = discord.Embed(title = "DANCE DANCE BABY!!".format(ctx.message.author.name))
    embed.set_image(url ="https://external-preview.redd.it/O344OQ3Tdkfy80TzwR0vUZcqRJYpI8JamgDgr-mOC74.gif?width=600&height=314.136125654&s=cfb769c9aa5197e112434eedebc5eec3df53fcd0 ")
    await ctx.send(f"Prefer mad Thanos or happy Thanos? ", embed = embed)
    await ctx.message.delete()
	
@client.command()
async def sleep(ctx):
    user = ctx.message.author 
    await user.add_roles(discord.utils.get(ctx.guild.roles, name = "Do not disturb"))
    embed = discord.Embed(title = "{0} Its sleeping time!".format(ctx.message.author.name))
    embed.set_image(url ="https://media.tenor.com/images/bed6d973f9d9b51b2e555e383eab3cb9/tenor.gif ")
    await ctx.send(f"You r now invisible {ctx.message.author.mention} ", embed = embed)
    await ctx.message.delete()

	
client.run(os.environ['TOKEN'])

