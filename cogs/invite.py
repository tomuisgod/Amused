import discord
from discord.ext import commands

client = discord.Client()


class Invite(commands.Cog):

    def __init__(self, client):
        self.client = client

    # loaded
    @commands.Cog.listener()
    async def on_ready(self):
        print("Invite.py loaded")

    # commands
    @commands.command()
    async def invite(self, ctx):
        embed = discord.Embed(title="Invite", color=discord.Color.blurple(),
                              url="https://discord.com/api/oauth2/authorize?client_id=732225428445462569&permissions=1593043030&scope=bot")
        embed.add_field(name="<:1147_WumpusHeart:748456654630289418> Thank you for your support!",
                        value="By inviting our bot to your server you help us grow."
                              " If you want to help us more, then use command `/vote`", inline=False)

        await ctx.send(embed=embed)

    @commands.command()
    async def vote(self, ctx):
        embed = discord.Embed(title="Vote", color=discord.Color.blurple(),
                              url="https://top.gg/bot/732225428445462569")
        embed.add_field(name="<:1147_WumpusHeart:748456654630289418> Thank you for your support!",
                        value="By voting for our bot on **top.gg** you help us grow."
                              " If you want to help us more, then use command `/invite`", inline=False)

        await ctx.send(embed=embed)

    @commands.command()
    async def website(self, ctx):
        embed = discord.Embed(title="Website", color=discord.Color.blurple(), url="http://amusedbot.glitch.me/webpage.html")

        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Invite(client))