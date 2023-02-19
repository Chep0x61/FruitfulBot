import discord
from discord.ext import commands

class Help(commands.Cog):

    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.command()
    async def help(self, ctx: commands.Context):
        embed = discord.Embed(title="Help Command",
                              description=f"WIP",
                              color=discord.Colour.from_rgb(234, 200, 115))
        await ctx.send(embed=embed)

async def setup(client):
    await client.add_cog(Help(client))