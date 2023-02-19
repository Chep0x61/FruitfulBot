import random
import discord
from discord.ext import commands

class Snowball(commands.Cog):

    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.command()
    async def snowball(self, ctx, member:discord.Member=None):
        if member is not None:
            await ctx.send(f"{member.mention} was hit by a snowball ! :snowman2:")
        else:
            await ctx.send(f"{random.choice(ctx.guild.members).mention} was hit by a snowball ! :snowman2:")
        await ctx.message.delete()

async def setup(client):
    await client.add_cog(Snowball(client))