import asyncio
import discord
import os

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
client = commands.Bot(command_prefix='!', intents=discord.Intents().all())

async def load(client):
    for filename in os.listdir('./Commands'):
        if filename.endswith('.py'):
            await client.load_extension(f'Commands.{filename[: -3]}')

async def main():
    await load(client)
    await client.start(os.getenv('token'))

asyncio.run(main())