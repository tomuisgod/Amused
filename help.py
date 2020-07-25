import discord
from discord.ext import commands

client = discord.Client()


class Help(commands.Cog):

    def __init__(self, client):
        self.client = client

    # loaded
    @commands.Cog.listener()
    async def on_ready(self):
        print("Help.py loaded")

    # command
    @commands.command()
    async def help(self, ctx):
        await ctx.send(":white_check_mark: | I sent you DM with help command!")

        embed = discord.Embed(title=" ", colour=discord.Color.blurple())
        embed.set_author(name="My prefix is / and I have 14 commands!", icon_url=self.client.user.avatar_url)
        embed.add_field(name=":monkey_face: Fun", value="`pp` | `iq` | `8b`", inline=False)
        embed.add_field(name=":gear: Information", value="`help` | `info`", inline=False)
        embed.add_field(name=":frame_photo: Photos", value="`waifus` | `shiba` | `dog` | `skin`", inline=False)
        embed.add_field(name=":hammer: Administration", value="`ban` | `kick` | `clear`", inline=False)
        embed.add_field(name=":test_tube: Development", value="`load` | `unload` | `reload`")
        await ctx.author.send(embed=embed)


def setup(client):
    client.add_cog(Help(client))
