import discord
import os
import asyncio
from discord.ext import commands

client = commands.Bot(command_prefix = '>')
client.remove_command('help')

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(game=discord.Game(name="Eating Webhooks 👻"))

@client.command()
async def ping():
    await client.say('Pong! :ping_pong:')



@client.command(pass_context=True)
async def request(ctx, *, remind):
    message = await client.say(f"{ctx.message.author.mention} Your request has been submitted! We will let you know if its approved.")
    await client.delete_message(ctx.message)
    await asyncio.sleep(5)
    await client.delete_message(message)
    author = ctx.message.author
    channel = author.server.get_channel('614814762890559498')
    embed = discord.Embed(
        colour=discord.Colour.gold()
    )
    embed.set_author(name="Submission For The Podcast")
    embed.add_field(name="A request has been made by:", value="{0}".format(author.mention), inline=False)
    embed.add_field(name="Message: ", value="{0}".format(remind), inline=False)
    await client.send_message(channel, embed=embed)


client.run(os.environ["TOKEN"])
