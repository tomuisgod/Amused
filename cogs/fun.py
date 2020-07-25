import discord
import requests
import json
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
    "Small IQ!",
    "Very small IQ!",
    "Your so dumb dude I don't honestly know If you can even read!",
    "Average IQ!",
    "Pretty good IQ!",
    "Your so smart!",
    "High IQ!",
    "Very high IQ!"

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
        await ctx.send("This is your pp: " + random.choice(pps))

    @commands.command()
    async def iq(self, ctx):
        await ctx.send(random.choice(iqs))

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



def setup(client):
    client.add_cog(Fun(client))
