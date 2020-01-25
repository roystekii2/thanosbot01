
#!/usr/bin/env python3
# -- coding: utf-8 --
import logging
import os
import random
import requests
import discord
from discord.ext import commands
from discord.utils import get

# you need this line, and you forgot it
logging.basicConfig(level='INFO')

client = commands.Bot(command_prefix="=", case_insensitive=True)
client.remove_command('help')
def C(ch:int):
    if ch == 586147813730025503 or ch == 605335008525156352 or ch == 587631308344262659 or ch == 592258548533166100:
        return 1 
    else:
        return 2
global c 
c = C
# do NOT use @client.event here, it breaks everything

@client.listen() 
async def on_message(message):
    nsfw_channel = client.get_channel(593050161467621395) 
    general = client.get_channel(586147813730025503) 
    if message.channel == nsfw_channel and not message.attachments:
        await message.delete()
    elif message.channel == general and message.attachments and not message.author.guild_permissions.administrator:
        await message.delete()
        
    
     
        


@client.command()
@commands.has_any_role("Admin", "Mod", "Chat Mod")
async def thanossnap(ctx, member : discord.member, *, reason=None): 
    await member.ban(reason=reason)
    await ctx.send('{0} was snapped out of existence!'.format(user))
    await ctx.message.delete()

@client.command() 
@commands.has_any_role("Admin", "Mod", "Chat Mod")
async def purge(ctx, amount=1):
    await ctx.channel.purge(limit=amount)
    await ctx.channel.send(f'Deleted {amount} messages')
    await ctx.message.delete()

@client.command() 
@commands.has_any_role("Admin", "Mod", "Chat Mod")
async def unmute(ctx, user: discord.Member):
    await user.remove_roles(discord.utils.get(ctx.guild.roles, name = "Muted"))
    await ctx.send('{0} has been unmuted!'.format(user))
    await ctx.message.delete()




@client.command() 
@commands.has_any_role("Admin", "Mod", "Chat Mod")
async def mute(ctx, user: discord.Member):
    await user.add_roles(discord.utils.get(ctx.guild.roles, name = "Muted"))
    await ctx.send('{0} has been unmuted!'.format(user))
    await ctx.message.delete()


@client.command()
async def jointheforce(ctx):
    global c 
    if c(ctx.channel.id) == 1:
        await ctx.send(f"Use this command in {client.get_channel(568398126671593496).mention}")
    else:
        user = ctx.message.author 
        await user.add_roles(discord.utils.get(ctx.guild.roles, name = "Thanos' Children"))
        embed = discord.Embed(title = "welcome {0} to the family!".format(ctx.message.author.name))
        embed.set_image(url ="https://static.comicvine.com/uploads/original/11113/111131285/6475508-9502292318-64162.gif ")
        await ctx.send("You are now my child...", embed = embed)
    await ctx.message.delete()
	
	
@client.command()
async def leavetheforce(ctx):
    global c 
    if c(ctx.channel.id) == 1:
        await ctx.send(f"Use this command in {client.get_channel(568398126671593496).mention}")
    else:
        user = ctx.message.author 
        await user.remove_roles(discord.utils.get(ctx.guild.roles, name = "Thanos' Children"))
        embed = discord.Embed(title = "Farewell {0} to the family... You are on your own now...".format(ctx.message.author.name))
        embed.set_image(url ="https://i1.wp.com/78.media.tumblr.com/b4171532756933ce3014e9ddffe0fbce/tumblr_pcp1aiorRo1sc0ffqo5_540.gif?w=605&ssl=1 ")
        await ctx.send(f"You have failed me... {ctx.message.author.mention} left the family...", embed = embed)
    await ctx.message.delete()

	
@client.command()
async def snap(ctx):
    global c 
    if c(ctx.channel.id) == 1:
        await ctx.send(f"Use this command in {client.get_channel(568398126671593496).mention}")
    else:
        user = ctx.message.author 
        embed = discord.Embed(title = "OH SNAP!".format(ctx.message.author.name))
        embed.set_image(url ="https://media1.tenor.com/images/e36fb32cfc3b63075adf0f1843fdc43a/tenor.gif?itemid=12502580 ")
        await ctx.send(f"I can do it with a snap of fingers, and you all cease to exist ", embed = embed)
    await ctx.message.delete()

@client.command()
async def thanoschildren(ctx):
    global c 
    if c(ctx.channel.id) == 1:
        await ctx.send(f"Use this command in {client.get_channel(568398126671593496).mention}")
    else:
        await ctx.send(f"current server members: {ctx.guild.member_count}")
    await ctx.message.delete()


@client.command()
async def thanosdance(ctx):
    global c 
    if c(ctx.channel.id) == 1:
        await ctx.send(f"Use this command in {client.get_channel(568398126671593496).mention}")
    else:
        user = ctx.message.author 
        embed = discord.Embed(title = "DANCE DANCE BABY!!".format(ctx.message.author.name))
        embed.set_image(url ="https://external-preview.redd.it/O344OQ3Tdkfy80TzwR0vUZcqRJYpI8JamgDgr-mOC74.gif?width=600&height=314.136125654&s=cfb769c9aa5197e112434eedebc5eec3df53fcd0 ")
        await ctx.send(f"Prefer mad Thanos or happy Thanos? ", embed = embed)
        await ctx.message.delete()
	
@client.command()
async def sleep(ctx):
    global c 
    if c(ctx.channel.id) == 3: #modified so it wont work anyway
        await ctx.send(f"Use this command in {client.get_channel(568398126671593496).mention}")
    else:
        user = ctx.message.author 
        await user.add_roles(discord.utils.get(ctx.guild.roles, name = "Do not disturb"))
        embed = discord.Embed(title = "{0} Its sleeping time!".format(ctx.message.author.name))
        embed.set_image(url ="https://media.tenor.com/images/bed6d973f9d9b51b2e555e383eab3cb9/tenor.gif ")
        await ctx.send(f"You r now invisible {ctx.message.author.mention} ", embed = embed)
        await ctx.message.delete()
	
@client.command()
async def wakeup(ctx):
    global c 
    if c(ctx.channel.id) == 3: #modified so it wont work anyway dont touch
        await ctx.send(f"Use this command in {client.get_channel(568398126671593496).mention}")
    else:
        user = ctx.message.author 
        await user.remove_roles(discord.utils.get(ctx.guild.roles, name = "Do not disturb"))
        embed = discord.Embed(title = "{0} Welcome back!".format(ctx.message.author.name))
        embed.set_image(url ="https://media2.giphy.com/media/ZlL9U0DNaOdFK/giphy.gif ")
        await ctx.send(f"You just woke up! {ctx.message.author.mention} ", embed = embed)
    await ctx.message.delete()

@client.command()
async def enterquantum(ctx):
    global c 
    if c(ctx.channel.id) == 1:
        await ctx.send(f"Use this command in {client.get_channel(568398126671593496).mention}")
    else:
        user = ctx.message.author 
        await user.add_roles(discord.utils.get(ctx.guild.roles, name = "Hot(NSFW)"))
        embed = discord.Embed(title = "{0}, Prepare yourself~~".format(ctx.message.author.name))
        embed.set_image(url ="https://imgix.bustle.com/uploads/image/2018/5/29/557a49a9-ccd7-4a93-8200-29af5c327b8d-tumblr_p7jzjhkadj1wonjtqo4_r1_540.gif ")
        await ctx.send(f"You are now entering the quantum realm... {ctx.message.author.mention} ", embed = embed)
    await ctx.message.delete()
	
@client.command()
async def exitquantum(ctx):
    global c 
    if c(ctx.channel.id) == 1:
        await ctx.send(f"Use this command in {client.get_channel(568398126671593496).mention}")
    else:
        user = ctx.message.author 
        await user.remove_roles(discord.utils.get(ctx.guild.roles, name = "Hot(NSFW)"))
        embed = discord.Embed(title = "{0} Goodbye~~ come back soon!".format(ctx.message.author.name))
        embed.set_image(url ="https://i.kinja-img.com/gawker-media/image/upload/s--MPWE1GzG--/c_scale,fl_progressive,q_80,w_800/xfyrealmcjruk6o3vqpu.gif ")
        await ctx.send(f"{ctx.message.author.mention}, you are now leaving the quantum realm... ", embed = embed)
    await ctx.message.delete()
	
@client.command()
async def thanosquotes(ctx):
    global c 
    print(c(ctx.channel.id))
    if c(ctx.channel.id) == 1:
        await ctx.send(f"Use this command in {client.get_channel(568398126671593496).mention}")
    else:
        member = ctx.message.author
        embed = discord.Embed(title = "Thanos' Famous Quotes".format(ctx.message.author.name))
        embed.set_image(url ="https://data.whicdn.com/images/326805782/original.gif ")
        messages = ["The end is near...", "You’re strong. But I could snap my fingers, and you’d all cease to exist.", "Fun isn’t something one considers when balancing the universe. But this… does put a smile on my face.","Stark… you have my respect. I hope the people of Earth will remember you.","I know what it's like to lose. To feel so desperately that you're right, yet to fail nonetheless. It's frightening, turns the legs to jelly. I ask you to what end? Dread it. Run from it. Destiny arrives all the same. And now it's here. Or should I say, I am."]
        message=random.choice(messages).format(member.mention)
        await ctx.send(message, embed=embed)
    await ctx.message.delete()



@client.command()
async def help(ctx):
    embed = discord.Embed(title="Ebony Maw", description="Thanos' bot. Lists of commands are:", color=0xeee657)

    embed.add_field(name="=snap", value="Display a snap gif", inline=False)
    embed.add_field(name="=thanoschildren", value="Display current server members", inline=False)
    embed.add_field(name="=thanosdance", value="Mmmm dance", inline=False)
    embed.add_field(name="=jointheforce", value="Gets you the role Thanos' Children, which you have to obey to Thanos at any time", inline=False)
    embed.add_field(name="=leavetheforce", value="Very straight forward, remove the Thanos' Children role", inline=False)
    embed.add_field(name="=sleep", value="Gives you the role Do Not Disturb to avoid any notifications", inline=False)
    embed.add_field(name="=wakeup", value="Back to normal", inline=False)
    embed.add_field(name="=enterquantum", value="Enter the NSFW channel for hots", inline=False)
    embed.add_field(name="=exitquantum", value="Back to normal and the hot channel disappeared", inline=False)
    embed.add_field(name="=thanosquotes", value="Says a random quote from Thanos", inline=False)
    
    await ctx.message.author.send(embed=embed)
    if ctx.guild: 
        await ctx.send("I sent you a DM!")
 
	
   

@client.command()
async def idk(ctx, *, a):
    if ctx.message.author.id in [258818862454276096, 457986700736462850]:
        await ctx.send(eval(a))
	
	
@client.command()
async def info(ctx):
    embed = discord.Embed(title="Name", description="Ebony Maw", color=0xeee657)
    embed.set_author(name="Ebony Maw", icon_url="https://images-ext-1.discordapp.net/external/k_qUq5L9Kz6rChxOXiYPZhCDOo6hblet5Vkdt-spSiM/%3Fsize%3D128/https/cdn.discordapp.com/avatars/597779593893642240/b3728edd9068d2df1a2ad48c3f87e5bb.png")
    embed.add_field(name="Creators", value="Roy&Lolidk", inline=False)
    embed.add_field(name="Server count", value=f"{len(client.guilds)}", inline=False)
    embed.add_field(name="Bot creation date", value=f"Mon, Jul 8, 2019 9:22 AM (GMT+9)", inline=False)
    await ctx.send(embed=embed)
    
@client.event
async def on_message(msg):
    if int(msg.author.id) == 554650679868915712:
        if "<@258818862454276096>" in msg.content:
            await msg.delete()
            await msg.channel.send("HA GOTEM")
    await client.process_commands(msg)






@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='Upgrading Thanos Tech| =help'))
	
client.run(os.environ['TOKEN'])
