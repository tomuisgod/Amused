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
            is_member_bot = "Yes!"
        else:
            is_member_bot = "No!"

        embed = discord.Embed(colour=member.color, timestamp=ctx.message.created_at)
        embed.set_author(name=f"{member.top_role} {member}")
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text="{}".format(ctx.message.author.name), icon_url=ctx.author.avatar_url)
        embed.add_field(name="**ID:**", value=f"||{member.id}||", inline=False)
        embed.add_field(name="Account has been created:",
                        value=member.created_at.strftime("%a, %d, %B, %Y, %I: %M, %p UTC"), inline=False)
        embed.add_field(name="Highest role:", value=member.top_role.mention, inline=False)
        embed.add_field(name="Bot?", value=is_member_bot, inline=False)

        await ctx.send(embed=embed)

    @commands.command()
    async def avatar(self, ctx, member:discord.Member):
        embed = discord.Embed(title=" ", color=discord.Color.blurple(), timestamp=ctx.message.created_at)
        embed.set_author(name=f"{member}")
        embed.set_image(url=member.avatar_url)
        embed.set_footer(text="{}".format(ctx.message.author.name), icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Profile(client))