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
    @commands.has_permissions(manage_messages=True)
    async def say(self, ctx, *, texts, amount=1):
        await ctx.channel.purge(limit=amount)

        embed = discord.Embed(title=texts, color=discord.Color.blurple(), timestamp=ctx.message.created_at)
        embed.set_author(name="{}".format(ctx.message.author.name), icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)

    @say.error
    async def say_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title="<:9830_no:748426943766069308> **Missing Argument! Please use correct form** `/say <text>`",
                                  color=discord.Color.red())

            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Say(client))
