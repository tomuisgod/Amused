import random
import requests
import youtube_dl
import discord
import json
import os

from discord.ext import commands

client = discord.Client()
client = commands.Bot(command_prefix="/")
client.remove_command("help")
token = "xxx"

with open('../../PycharmProjects/tomu/words.txt') as file:
    file = file.read().split()

pps = [
    "You don't have one!",
    "8=D",
    "8==D",
    "8===D",
    "8====D",
    "8======D",
    "8=======D",
    "8=========D",
    "8===========D",
    "8================D",
    "8===================D",
    "8===============================D  (largets possible :hot_face:)"
]


iqs = [
    "Small IQ!",
    "Very small IQ!",
    "Your so dumb dude I don't honestly know If you can even read!",
    "Average IQ!",
    "Pretty good IQ!",
    "Your so smart!",
    "High IQ!",
    "Very high IQ!"

]



@client.event #zaciatok
async def on_ready():
    print("-------------")
    print(client.user.name)
    print(client.user.id)
    print(discord.__version__)
    print(client.latency * 1000)
    print("-------------")


    await client.change_presence(activity=discord.Game("/help"))

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(title=":x: **Command not found! Try `/help`**", color=discord.Color.red())
        await ctx.send(embed=embed)

    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(title=":x: **You don't have enough permissions to execute this command!**", color=discord.Color.red())
        await ctx.send(embed=embed)

    if isinstance(error, commands.BotMissingPermissions):
        embed = discord.Embed(title=":x: **Bot don't have enough permission to execute this command!**", color=discord.Color.red())
        await ctx.send(embed=embeda)


@client.command()
async def pp(ctx):
    await ctx.send("This is your pp: " + random.choice(pps))

@client.command()
async def iq(ctx):
    await ctx.send(random.choice(iqs))


@client.command(aliases=["8b"])
async def _8ball(ctx, *, question):
    responses = [
        "Sure!",
        "Nahhh!",
        "I don't know dude!",
        "100%!!",
        "Not a chance!",
        "Ask me later please!",
        "No.",
        "Yes.",
        "It's possible!",
        "I can't answer this right now!"
    ]

    embed = discord.Embed(title="**8ball**", color=discord.Color.blurple(), timestamp=ctx.message.created_at)
    embed.add_field(name=" Q&A ",
                    value=f"**Question:** {question}\n **Answer:** {random.choice(responses)}")
    embed.set_footer(text="{}".format(ctx.message.author.name), icon_url=ctx.author.avatar_url)

    await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    embed = discord.Embed(title=":hammer: **Member has been banned!**", colour=discord.Color.red())

    await ctx.send(embed=embed)


@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    embed = discord.Embed(title=":hammer: **Member has been kicked!**", color=discord.Color.red())

    await ctx.send(embed=embed)


@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=10):
    await ctx.channel.purge(limit=amount)
    embed = discord.Embed(title=":white_check_mark: **Selected amount of messages has been deleted!**", color=discord.Color.green())

    await ctx.send(embed=embed)

@client.command()
async def skin(ctx, nick):
    embed = discord.Embed(title="Skin of play {}".format(nick),
                          description="[Click here to download the skin!](https://minotar.net/armor/body/{})".format(nick),
                          color=discord.Color.blurple())

    embed.set_image(url="https://minotar.net/armor/body/{}".format(nick))
    embed.set_footer(text="Skin requested by {}".format(ctx.message.author.name), icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)


@client.command()
@commands.is_owner()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    embed = discord.Embed(title=f'Loaded `{extension}`!', color=discord.Color.gold())
    await ctx.send(embed=embed)


@client.command()
@commands.is_owner()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    embed = discord.Embed(title=f'Unloaded `{extension}`!', color=discord.Color.gold())
    await ctx.send(embed=embed)


@client.command(
    name='reload', description="Reload all/one of the bots cogs!"
)
@commands.is_owner()
async def reload(ctx, cog=None):
    if not cog:
        # No cog, means we reload all cogs
        async with ctx.typing():
            embed = discord.Embed(
                title="Reloading all cogs!",
                color=discord.Color.blurple(),
                timestamp=ctx.message.created_at
            )
            for ext in os.listdir("./cogs/"):
                if ext.endswith(".py") and not ext.startswith("_"):
                    try:
                        client.unload_extension(f"cogs.{ext[:-3]}")
                        client.load_extension(f"cogs.{ext[:-3]}")
                        embed.add_field(
                            name=f"Reloaded: `{ext}`", value='\uFEFF', inline=False)
                    except Exception as e:
                        embed.add_field(
                            name=f"Failed to reload: `{ext}`", value=e, inline=False)
                    await asyncio.sleep(0.5)
            await ctx.send(embed=embed)
    else:
        # reload the specific cog
        async with ctx.typing():
            embed = discord.Embed(
                title="Reloading all cogs!",
                color=discord.Color.gold(),
                timestamp=ctx.message.created_at
            )
            ext = f"{cog.lower()}.py"
            if not os.path.exists(f"./cogs/{ext}"):
                # if the file does not exist
                embed.add_field(
                    name=f"Failed to reload: `{ext}`",
                    value="This cog does not exist.",
                    inline=False
                )

            elif ext.endswith(".py") and not ext.startswith("_"):
                try:
                    client.unload_extension(f"cogs.{ext[:-3]}")
                    client.load_extension(f"cogs.{ext[:-3]}")
                    embed.add_field(
                        name=f"Reloaded: `{ext}`", value='\uFEFF', inline=False)
                except Exception:
                    desired_trace = traceback.format_exc()
                    embed.add_field(
                        name=f"Failed to reload: `{ext}`", value=desired_trace, inline=False)
            await ctx.send(embed=embed)


for filename in os.listdir('./cogs/'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


client.run(token)