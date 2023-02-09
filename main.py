import asyncio
import discord
import os

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
client = commands.Bot(command_prefix='!', intents=discord.Intents().all())

async def load_commands(client):
    for filename in os.listdir('./Commands'):
        if filename.endswith('.py'):
            await client.load_extension(f'Commands.{filename[: -3]}')

async def load_events(client):
    for filename in os.listdir('./Events'):
        if filename.endswith('.py'):
            await client.load_extension(f'Events.{filename[: -3]}')

async def main():
    await load_events(client)
    await load_commands(client)
    await client.start(os.getenv('token'))

asyncio.run(main())