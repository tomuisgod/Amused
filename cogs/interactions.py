import discord
import requests
import json
from discord.ext import commands

client = discord.Client()


class Interactions(commands.Cog):

    def __init__(self, client):
        self.client = client

    # loaded
    @commands.Cog.listener()
    async def on_ready(self):
        print("Interactions.py loaded")

    # command

    @commands.command()
    async def dance(self, ctx):
        r = requests.get("https://waifu.pics/api/dance")
        res = r.content
        res = json.loads(res)
        embed = discord.Embed(title=" ", color=discord.Color.blurple(), timestamp=ctx.message.created_at)
        embed.set_image(url=res["url"])
        embed.set_footer(text="{}".format(ctx.message.author.name), icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)

    @commands.command()
    async def hug(self, ctx):
        r = requests.get("https://waifu.pics/api/hug")
        res = r.content
        res = json.loads(res)
        embed = discord.Embed(title=" ", color=discord.Color.blurple(), timestamp=ctx.message.created_at)
        embed.set_image(url=res["url"])
        embed.set_footer(text="{}".format(ctx.message.author.name), icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Interactions(client))