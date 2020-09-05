import discord
from discord.ext import commands

client = discord.Client()


class QOTD(commands.Cog):

    def __init__(self, client):
        self.client = client

    # loaded

    @commands.Cog.listener()
    async def on_ready(self):
        print("QOTD.py loaded")

    # command

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def qotdadd(self, ctx, question, amount=1):
        await ctx.channel.purge(limit=amount)

        embed = discord.Embed(title="<:1147_WumpusHeart:748456654630289418> **QOTD**", color=discord.Color.green(), timestamp=ctx.message.created_at)
        embed.add_field(name="This is the question for this day:", value=question)
        embed.set_footer(text="{}".format(ctx.message.author.name), icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)

    @qotdadd.error
    async def qotdadd_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title="<:9830_no:748426943766069308> **Missing Argument! Please use correct form** `/qotdadd <text>`",
                                  color=discord.Color.red())

            await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def qotdch(self, ctx, *, feedback, amount=1):
        await ctx.channel.purge(limit=amount)

        embed = discord.Embed(title="<:1147_WumpusHeart:748456654630289418> **QOTD**", color=discord.Color.gold(),
                              timestamp=ctx.message.created_at)
        embed.add_field(name="Vote and choose QOTD for next day", value=feedback)
        embed.set_footer(text="{}".format(ctx.message.author.name), icon_url=ctx.author.avatar_url)

        one = "<:blob1:750279045211488407>"
        two = "<:blob2:750279067605008434>"
        three = "<:blob3:750279089629298758>"

        msg = await ctx.send(embed=embed)
        await msg.add_reaction(one)
        await msg.add_reaction(two)
        await msg.add_reaction(three)

    @qotdch.error
    async def qotdch_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                title="<:9830_no:748426943766069308> **Missing Argument! Please use correct form** `q!qotdch <text>`",
                color=discord.Color.red())

            await ctx.send(embed=embed)

    @commands.command()
    async def qotdinfo(self, ctx):
        embed = discord.Embed(title="<:1147_WumpusHeart:748456654630289418>**QOTD Info**", color=discord.Color.blurple(), timestamp=ctx.message.created_at)
        embed.add_field(name="What is QOTD?", value="QOTD is abbreviation of `Question of the day`", inline=False)
        embed.add_field(name="Who can use QOTD?", value="QOTD is for everyone, but only staff members with "
                                                        "`manage_messages` can add QOTD", inline=False)

        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(QOTD(client))