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
            embed = discord.Embed(title="<:9830_no:748426943766069308> **Missing Argument! Please use correct form** `/ban @mention`", color=discord.Color.red())

            await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        embed = discord.Embed(title=":hammer: **Member has been kicked!**", color=discord.Color.red(), timestamp=ctx.message.created_at)
        embed.set_footer(text="{}".format(ctx.message.author.name), icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=10):
        await ctx.channel.purge(limit=amount)
        embed = discord.Embed(title="<:9358_yes_tick:748426928347938897> Messages has been deleted!", color=discord.Color.green())
        await ctx.send(embed=embed)


    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title="<:9830_no:748426943766069308> **Missing Argument! Please use correct form** `/kick @mention`",
                                  color=discord.Color.red())

            await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, member:discord.Member, *, reason=None):
        await member.unban(reason=reason)
        embed = discord.Embed(title=":hammer: **Member has been unbaned!**", color=discord.Color.red(), timestamp=ctx.message.created_at)
        embed.set_footer(text="{}".format(ctx.message.author.name), icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def deletechannel(self, ctx, channel: discord.guild.TextChannel):
        await channel.delete()

def setup(client):
    client.add_cog(Admin(client))
