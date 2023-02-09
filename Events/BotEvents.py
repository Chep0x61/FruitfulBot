import discord
from discord.ext import commands

class BotEvents(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot Started")
        await self.client.change_presence(activity=discord.Game(name="Trying to be helpful ⚡"))

async def setup(client):
    await client.add_cog(BotEvents(client))