import discord
from discord.ext import commands

client = discord.Client()

class Say(commands.Cog):

    def __init__(self, client):
        self.client = client

    # loaded
    @commands.Cog.listener()
    async def on_ready(self):
        print("Say.py loaded")

    # command
    @commands.command()
    async def say(self, ctx, *, texts, amount=1):
        await ctx.channel.purge(limit=amount)

        embed = discord.Embed(title=texts, color=discord.Color.blurple(), timestamp=ctx.message.created_at)
        embed.set_author(name="{}".format(ctx.message.author.name), icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Say(client))