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
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        embed = discord.Embed(title=":hammer: **Member has been banned!**", colour=discord.Color.red(), timestamp=ctx.message.created_at)
        embed.set_footer(text="{}".format(ctx.message.author.name), icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed= discord.Embed(title="**Missing Argument! Please use correct form** `/ban @mention`", color=discord.Color.red())

            await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        embed = discord.Embed(title=":hammer: **Member has been kicked!**", color=discord.Color.red(), timestamp=ctx.message.created_at)
        embed.set_footer(text="{}".format(ctx.message.author.name), icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title="**Missing Argument! Please use correct form** `/kick @mention`",
                                  color=discord.Color.red())

            await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, member:discord.Member, *, reason=None):
        await member.unban(reason=reason)
        embed = discord.Embed(title=":hammer: **Member has been unbaned!**", color=discord.Color.red(), timestamp=ctx.message.created_at)
        embed.set_footer(text="{}".format(ctx.message.author.name), icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Admin(client))
