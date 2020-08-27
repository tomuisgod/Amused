import discord
import requests
import json
import random
from discord.ext import commands

client = discord.Client()

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
    "...small!",
    "...very small!",
    "...your so dumb dude I don't honestly know If you can even read!",
    "...average!",
    "...pretty good!",
    "...your so smart that I can't even measure your IQ!",
    "...high!",
    "...very high!"

]

love = [
    "0%"
    "32%"
    "48%"
    "15%"
    "87%"
    "47%"
    "14%"
    "0%"
    "41%"
    "100%"
    "49%"
    "78%"
    "12%"
    "1%"
    "26%"
    "36%"
    "46%"
    "76%"
    "44%"
]

class Fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    # loaded
    @commands.Cog.listener()
    async def on_ready(self):
        print("Fun.py loaded")

    # commands

    @commands.command()
    async def pp(self, ctx):
        embed = discord.Embed(title="Pp meter", color=discord.Color.blurple(), timestamp=ctx.message.created_at)
        embed.add_field(name="This is your penis", value=f"{random.choice(pps)}")
        embed.set_footer(text="{}".format(ctx.message.author.name), icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)


    @commands.command()
    async def iq(self, ctx):
        embed = discord.Embed(title="IQ meter", color=discord.Color.blurple(), timestamp=ctx.message.created_at)
        embed.add_field(name="Your IQ is...", value=f"{random.choice(iqs)}")
        embed.set_footer(text="{}".format(ctx.message.author.name), icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)

    @commands.command(aliases=["8b"])
    async def _8ball(self, ctx, *, question):
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

    @_8ball.error
    async def _8ball_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title="**Missing Argument! Please use correct form** `/8ball <question>`", color=discord.Color.red())
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Fun(client))
