import discord
from discord.ext import commands

client = discord.Client()


class Admin(commands.Cog):

    def __init__(self, client):
        self.client = client

    # loaded
    @commands.Cog.listener()
    async def on_ready(self):
        print("Admin.py loaded")

    # command
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        embed = discord.Embed(title=":hammer: **Member has been banned!**", colour=discord.Color.red(), timestamp=ctx.message.created_at)
        embed.set_footer(text="{}".format(ctx.message.author.name), icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        embed = discord.Embed(title=":hammer: **Member has been kicked!**", color=discord.Color.red(), timestamp=ctx.message.created_at)
        embed.set_footer(text="{}".format(ctx.message.author.name), icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(ctx, amount=10):
        await ctx.channel.purge(limit=amount)
        embed = discord.Embed(title=":white_check_mark: **Selected amount of messages has been deleted!**",
                              color=discord.Color.green())

        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Admin(client))