import discord
from discord.ext import commands

client = discord.Client()

class Profile(commands.Cog):

    def __init__(self, client):
        self.client = client

    # loaded
    @commands.Cog.listener()
    async def on_ready(self):
        print("Profile.py loaded")

    # command
    @commands.command()
    async def profile(self, ctx, member: discord.Member):
        roles = [role for role in member.roles]

        is_member_bot = member.bot
        if is_member_bot == True:
            is_member_bot = "<:9358_yes_tick:748426928347938897>"
        else:
            is_member_bot = "<:9830_no:748426943766069308>"


        embed = discord.Embed(colour=member.color, timestamp=ctx.message.created_at)
        embed.set_author(name=f"{member.top_role} {member}")
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text="{}".format(ctx.message.author.name), icon_url=ctx.author.avatar_url)
        embed.add_field(name="<:5681_certified_blue:748426802804031578> **ID:**", value=f"||{member.id}||", inline=False)
        embed.add_field(name="<:3832_status_online:748426740673806377> **Status:**", value=f"{member.status}")
        embed.add_field(name="Account has been created:",
                        value=member.created_at.strftime("%a, %d, %B, %Y, %I: %M, %p UTC"), inline=False)
        embed.add_field(name="<:8840_brawl_stars_trophy:748459981573193749> Highest role:", value=member.top_role.mention, inline=False)
        embed.add_field(name="<:4713_ubot:748458596748230656> Bot?", value=is_member_bot, inline=False)

        await ctx.send(embed=embed)

    @profile.error
    async def profile_error(self, ctx, error):
        embed = discord.Embed(title="**Missing Argument! Please use correct form** `/profile @mention`",
                              color=discord.Color.red())
        await ctx.send(embed=embed)

    @commands.command()
    async def avatar(self, ctx, member:discord.Member):
        embed = discord.Embed(title=" ", color=discord.Color.blurple(), timestamp=ctx.message.created_at)
        embed.set_author(name=f"{member}")
        embed.set_image(url=member.avatar_url)
        embed.set_footer(text="{}".format(ctx.message.author.name), icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)

    @avatar.error
    async def avatar_error(self, ctx, error):
        embed = discord.Embed(title="**Missing Argument! Please use correct form** `/avatar @mention`",
                              color=discord.Color.red())
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Profile(client))
