import discord
import requests
import asyncio
import json
from discord.ext import commands

client = discord.Client()


class NSFW(commands.Cog):

    def __init__(self, client):
        self.client = client

    # loaded
    @commands.Cog.listener()
    async def on_ready(self):
        print("NSFW.py")

    # command

    @commands.command()
    async def sfw(self, ctx):
        if ctx.channel.is_nsfw() == False:
            embed = discord.Embed(title="<:9830_no:748426943766069308> You can't use NSFW commands in non NSFW channels!", color=discord.Color.red())

            await ctx.send(embed=embed)

        else:
            r = requests.get("https://waifu.pics/api/sfw")
            res = r.content
            res = json.loads(res)
            embed = discord.Embed(title=" ", color=discord.Color.blurple(), timestamp=ctx.message.created_at)
            embed.set_image(url=res["url"])
            embed.set_footer(text="{}".format(ctx.message.author.name), icon_url=ctx.author.avatar_url)

            await ctx.send(embed=embed)

    @commands.command()
    async def nsfw(self, ctx):
        if ctx.channel.is_nsfw() == False:
            embed = discord.Embed(title="<:9830_no:748426943766069308> You can't use NSFW commands in non NSFW channels!", color=discord.Color.red())

            await ctx.send(embed=embed)

        else:
            r = requests.get("https://waifu.pics/api/nsfw")
            res = r.content
            res = json.loads(res)
            embed = discord.Embed(title=" ", color=discord.Color.blurple(), timestamp=ctx.message.created_at)
            embed.set_image(url=res["url"])
            embed.set_footer(text="{}".format(ctx.message.author.name), icon_url=ctx.author.avatar_url)

            await ctx.send(embed=embed)

    @commands.command()
    async def lewdneko(self, ctx):
        if ctx.channel.is_nsfw() == False:
            embed = discord.Embed(
                title="<:9830_no:748426943766069308> You can't use NSFW commands in non NSFW channels!",
                color=discord.Color.red())

            await ctx.send(embed=embed)
        else:
            r = requests.get("https://waifu.pics/api/lewdneko")
            res = r.content
            res = json.loads(res)
            embed = discord.Embed(title=" ", color=discord.Color.blurple(), timestamp=ctx.message.created_at)
            embed.set_image(url=res["url"])
            embed.set_footer(text="{}".format(ctx.message.author.name), icon_url=ctx.author.avatar_url)

            await ctx.send(embed=embed)



def setup(client):
    client.add_cog(NSFW(client))
