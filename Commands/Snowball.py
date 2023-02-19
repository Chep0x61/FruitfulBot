import random
import discord
from discord.ext import commands

class Snowball(commands.Cog):

    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.command()
    async def snowball(self, ctx):
        await ctx.send(f"{random.choice(ctx.guild.members).mention}")
        await ctx.message.delete()

async def setup(client):
    await client.add_cog(Snowball(client))