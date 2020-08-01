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

    @commands.command()
    async def kiss(self, ctx):
        r = requests.get("https://waifu.pics/api/kiss")
        res = r.content
        res = json.loads(res)
        embed = discord.Embed(title=" ", color=discord.Color.blurple(), timestamp=ctx.message.created_at)
        embed.set_image(url=res["url"])
        embed.set_footer(text="{}".format(ctx.message.author.name), icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)

    @commands.command()
    async def bully(self, ctx):
        r = requests.get("https://waifu.pics/api/bully")
        res = r.content
        res = json.loads(res)
        embed = discord.Embed(title=" ", color=discord.Color.blurple(), timestamp=ctx.message.created_at)
        embed.set_image(url=res["url"])
        embed.set_footer(text="{}".format(ctx.message.author.name), icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)

    @commands.command()
    async def cry (self, ctx):
        r = requests.get("https://waifu.pics/api/cry")
        res = r.content
        res = json.loads(res)
        embed = discord.Embed(title=" ", color=discord.Color.blurple(), timestamp=ctx.message.created_at)
        embed.set_image(url=res["url"])
        embed.set_footer(text="{}".format(ctx.message.author.name), icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)

    @commands.command()
    async def pat(self, ctx):
        r = requests.get("https://waifu.pics/api/pat")
        res = r.content
        res = json.loads(res)
        embed = discord.Embed(title=" ", color=discord.Color.blurple(), timestamp=ctx.message.created_at)
        embed.set_image(url=res["url"])
        embed.set_footer(text="{}".format(ctx.message.author.name), icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)

    @commands.command()
    async def highfive(self, ctx):
        r = requests.get("https://waifu.pics/api/highfive")
        res = r.content
        res = json.loads(res)
        embed = discord.Embed(title=" ", color=discord.Color.blurple(), timestamp=ctx.message.created_at)
        embed.set_image(url=res["url"])
        embed.set_footer(text="{}".format(ctx.message.author.name), icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)

    @commands.command()
    async def bite(self, ctx):
        r = requests.get("https://waifu.pics/api/bite")
        res = r.content
        res = json.loads(res)
        embed = discord.Embed(title=" ", color=discord.Color.blurple(), timestamp=ctx.message.created_at)
        embed.set_image(url=res["url"])
        embed.set_footer(text="{}".format(ctx.message.author.name), icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)

    @commands.command()
    async def slap(self, ctx):
        r = requests.get("https://waifu.pics/api/slap")
        res = r.content
        res = json.loads(res)
        embed = discord.Embed(title=" ", color=discord.Color.blurple(), timestamp=ctx.message.created_at)
        embed.set_image(url=res["url"])
        embed.set_footer(text="{}".format(ctx.message.author.name), icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Interactions(client))
