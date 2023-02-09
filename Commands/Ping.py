import discord
from discord.ext import commands

class Ping(commands.Cog):

    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.command()
    async def ping(self, ctx: commands.Context):
        """
        Pong!
        """
        embed = discord.Embed(title="Ping Command",
                              description=f"🏓 My latency is about **{round(self.client.latency * 1000)} "
                                          f"ms**.\nFortunately, I'm still alive ! :rainbow:",
                              color=discord.Colour.from_rgb(234, 200, 115))
        await ctx.send(embed=embed)

async def setup(client):
    await client.add_cog(Ping(client))