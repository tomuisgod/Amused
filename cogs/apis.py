import discord
import requests
import json
from discord.ext import commands

client = discord.Client()


class API(commands.Cog):

    def __init__(self, client):
        self.client = client

    # loaded
    @commands.Cog.listener()
    async def on_ready(self):
        print("Apis.py loaded")

    # command

    @commands.command()
    async def waifus(self, ctx):
        r = requests.get("https://waifu.pics/api/sfw")
        res = r.content
        res = json.loads(res)
        embed = discord.Embed(title=" ", color=discord.Color.blurple(), timestamp=ctx.message.created_at)
        embed.set_image(url=res["url"])
        embed.set_footer(text="{}".format(ctx.message.author.name), icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)

    @commands.command()
    async def shiba(self, ctx):
        r = requests.get("http://shibe.online/api/shibes?count=1&urls=true&httpsUrls=true")
        res = r.content
        res = json.loads(res)
        embed = discord.Embed(title=" ", color=discord.Color.blurple(), timestamp=ctx.message.created_at)
        embed.set_image(url=res[0])
        embed.set_footer(text="{}".format(ctx.message.author.name), icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)

    @commands.command()
    async def dog(self, ctx):
        r = requests.get("https://api.alexflipnote.dev/dogs")
        res = r.content
        res = json.loads(res)
        embed = discord.Embed(title=" ", color=discord.Color.blurple(), timestamp=ctx.message.created_at)
        embed.set_image(url=res["file"])
        embed.set_footer(text="{}".format(ctx.message.author.name), icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)

    @commands.command()
    async def meme(self, ctx):
        r = requests.get("https://ronreiter-meme-generator.p.rapidapi.com/meme")
        res = r.content
        res = json.loads(res)
        embed = discord.Embed(title=" ", color=discord.Color.blurple(), timestamp=ctx.message.created_at)
        embed.set_image(url=res["GET"])
        embed.set_footer(text="{}".format(ctx.message.author.name), icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)

    @commands.command()
    async def skin(self, ctx, nick):
        embed = discord.Embed(title="Skin of player {}".format(nick),
                              description="[Click here to download the skin!](https://minotar.net/armor/body/{})".format(
                                  nick),
                              color=discord.Color.blurple())

        embed.set_image(url="https://minotar.net/armor/body/{}".format(nick))
        embed.set_footer(text="Skin requested by {}".format(ctx.message.author.name), icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @skin.error
    async def skin_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title="<:9830_no:748426943766069308> **Missing Argument! Please use correct form** `/skin Nick`",
                                  color=discord.Color.red())
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(API(client))
