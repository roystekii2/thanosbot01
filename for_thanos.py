#!/usr/bin/env python3
# -- coding: utf-8 --
import logging
import os

from discord.ext import commands

# you need this line, and you forgot it
logging.basicConfig(level='INFO')

import discord
from discord.ext import commands
client = commands.Bot(command_prefix = "?")
@client.command(aliases = ["amigo"])
async def Amigo(ctx):
    await ctx.send(f"I Love You 3000, {ctx.message.author.mention}")
@client.command()
async def breed(ctx):
    await ctx.send("I was a Miniature Pinscher!")
@client.command()
async def fruit(ctx):
    await ctx.send("My favorite fruit is Apple!")
client.run("NjA1MzQ0Njk2MDA4NDQxODU3.XUBLTQ.3Ex_nVLLH4zcKRAK3bc_09Q9ps0")
