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
    async def hug(self, ctx, member: discord.Member):
        r = requests.get("https://waifu.pics/api/hug")
        res = r.content
        res = json.loads(res)
        embed = discord.Embed(title=f"**{ctx.message.author}** hugs **{member}**", color=discord.Color.blurple(), timestamp=ctx.message.created_at)
        embed.set_image(url=res["url"])
        embed.set_footer(text="{}".format(ctx.message.author.name), icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)

    @hug.error
    async def hug_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title="**Missing Argument! Please use correct form** `/hug @mention`",
                                  color=discord.Color.red())
            await ctx.send(embed=embed)

    @commands.command()
    async def kiss(self, ctx, member: discord.Member):
        r = requests.get("https://waifu.pics/api/kiss")
        res = r.content
        res = json.loads(res)
        embed = discord.Embed(title=f"**{ctx.message.author}** kisses **{member}**", color=discord.Color.blurple(), timestamp=ctx.message.created_at)
        embed.set_image(url=res["url"])
        embed.set_footer(text="{}".format(ctx.message.author.name), icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)

    @kiss.error
    async def kiss_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title="**Missing Argument! Please use correct form** `/kiss @mention`",
                                  color=discord.Color.red())
            await ctx.send(embed=embed)

    @commands.command()
    async def bully(self, ctx, member: discord.Member):
        r = requests.get("https://waifu.pics/api/bully")
        res = r.content
        res = json.loads(res)
        embed = discord.Embed(title=f"**{ctx.message.author}** bullies **{member}**", color=discord.Color.blurple(), timestamp=ctx.message.created_at)
        embed.set_image(url=res["url"])
        embed.set_footer(text="{}".format(ctx.message.author.name), icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)

    @bully.error
    async def bully_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title="**Missing Argument! Please use correct form** `/bully @mention`",
                                  color=discord.Color.red())
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
    async def blush(self, ctx):
        r = requests.get("https://waifu.pics/api/pat")
        res = r.content
        res = json.loads(res)
        embed = discord.Embed(title=" ", color=discord.Color.blurple(), timestamp=ctx.message.created_at)
        embed.set_image(url=res["url"])
        embed.set_footer(text="{}".format(ctx.message.author.name), icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)

    @commands.command()
    async def highfive(self, ctx, member: discord.Member):
        r = requests.get("https://waifu.pics/api/highfive")
        res = r.content
        res = json.loads(res)
        embed = discord.Embed(title=f"**{ctx.message.author}** gives highfive to **{member}**", color=discord.Color.blurple(), timestamp=ctx.message.created_at)
        embed.set_image(url=res["url"])
        embed.set_footer(text="{}".format(ctx.message.author.name), icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)

    @highfive.error
    async def highfive_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title="**Missing Argument! Please use correct form** `/highfive @mention`",
                                  color=discord.Color.red())
            await ctx.send(embed=embed)

    @commands.command()
    async def bite(self, ctx, member: discord.Member):
        r = requests.get("https://waifu.pics/api/bite")
        res = r.content
        res = json.loads(res)
        embed = discord.Embed(title=f"**{ctx.message.author}** bites **{member}**", color=discord.Color.blurple(), timestamp=ctx.message.created_at)
        embed.set_image(url=res["url"])
        embed.set_footer(text="{}".format(ctx.message.author.name), icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)

    @bite.error
    async def bite_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title="**Missing Argument! Please use correct form** `/bite @mention`",
                                  color=discord.Color.red())
            await ctx.send(embed=embed)

    @commands.command()
    async def slap(self, ctx, member: discord.Member):
        r = requests.get("https://waifu.pics/api/slap")
        res = r.content
        res = json.loads(res)
        embed = discord.Embed(title=f"**{ctx.message.author}** slaps **{member}**", color=discord.Color.blurple(), timestamp=ctx.message.created_at)
        embed.set_image(url=res["url"])
        embed.set_footer(text="{}".format(ctx.message.author.name), icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)

    @slap.error
    async def slap_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title="**Missing Argument! Please use correct form** `/slap @mention`",
                                  color=discord.Color.red())
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Interactions(client))
