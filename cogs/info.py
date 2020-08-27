import discord
from discord.ext import commands

client = discord.Client()


class Info(commands.Cog):

    def __init__(self, client):
        self.client = client

    # loaded
    @commands.Cog.listener()
    async def on_ready(self):
        print("Info.py loaded")

    # command
    @commands.command()
    async def info(self, ctx):
        embed = discord.Embed(title="<:4228_discord_bot_dev:748426660478451803> **Info**", color=discord.Color.blurple())
        embed.add_field(name="`Ping:` ", value=f"**{round(self.client.latency * 1000)}** ms", inline=False)
        embed.add_field(name="`Discord.py version: `", value=f"**{discord.__version__}**", inline=False)
        embed.add_field(name="`Bot version:` ", value="**0.1.2**", inline=False)
        embed.add_field(name="`Bot developer:`", value="**bomu#1979**")
        embed.set_footer(text=f"{self.client.user.name}",
                         icon_url=self.client.user.avatar_url)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Info(client))
