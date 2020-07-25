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
        r = requests.get("https://api.deepai.org/api/waifu2x")
        res = r.content
        res = json.loads(res)
        embed = discord.Embed(title=" ", color=discord.Color.blurple())
        embed.set_image(url=res["image"])
        embed.set_footer(text="{}".format(ctx.message.author.name), icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)

    @commands.command()
    async def shiba(self, ctx):
        r = requests.get("http://shibe.online/api/shibes?count=1&urls=true&httpsUrls=true")
        res = r.content
        res = json.loads(res)
        embed = discord.Embed(title="**Random Shiba**", color=discord.Color.blurple(), timestamp=ctx.message.created_at)
        embed.set_image(url=res[0])
        embed.set_footer(text="{}".format(ctx.message.author.name), icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)

    @commands.command()
    async def dog(self, ctx):
        r = requests.get("https://api.alexflipnote.dev/dogs")
        res = r.content
        res = json.loads(res)
        embed = discord.Embed(title="**Random dog**", color=discord.Color.blurple(), timestamp=ctx.message.created_at)
        embed.set_image(url=res["file"])
        embed.set_footer(text="{}".format(ctx.message.author.name), icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(API(client))