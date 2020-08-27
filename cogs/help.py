import discord
from discord.ext import commands

client = discord.Client()


class Help(commands.Cog):

    def __init__(self, client):
        self.client = client

    # loaded
    @commands.Cog.listener()
    async def on_ready(self):
        print("Help.py loaded")

    # command
    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(title=" ", colour=discord.Color.blurple())
        embed.set_author(name="My prefix is / and I have 27 commands!", icon_url=self.client.user.avatar_url)
        embed.add_field(name="<:5574_WumpusGamer:748456675945742366> Fun", value="`pp` | `iq` | `8b` | `say` ", inline=False)
        embed.add_field(name="<:9852_wumpus:748456487793197116> Activities", value="`dance` | `blush` | `cry`")
        embed.add_field(name="<:1147_WumpusHeart:748456654630289418> Interactions", value=" `hug` | `kiss` | `bully` | "
                                                            "`highfive` | `bite` | `slap`", inline=False)
        embed.add_field(name="<:4228_discord_bot_dev:748426660478451803> Information", value="`help` | `info` | `profile` | `avatar`", inline=False)
        embed.add_field(name="<:1618_users_logo:748456867843539076> Photos", value="`waifus` | `shiba` | `dog` | `skin` | `meme`", inline=False)
        embed.add_field(name="<:5864_WumpusCrown:748456700247539754> Administration", value="`ban` | `kick` | `clear`", inline=False)
        embed.add_field(name="<:9552_BugHunterLvl2:748426887075856445> Development", value="`load` | `unload` | `reload`")

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Help(client))
