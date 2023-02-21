import discord
from discord.ext import commands

class Help(commands.Cog):

    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.command()
    async def help(self, ctx: commands.Context):
        embed = discord.Embed(title="Help Command",
                              description=f"**Don't forget our command prefix is `!`**\n **`?` means it's not mandatory.**",
                              color=discord.Colour.from_rgb(234, 200, 115))

        embed.add_field(name='Cs:', value='Share your csgo ip server.\nExample: `cs <ip:port>`', inline=False)

        embed.add_field(name='Info:', value='Get infos on you or another member.\nExample: `Info <target?>`', inline=False)

        embed.add_field(name='Meme:', value='Get a top random Meme from Reddit.\nExample: `meme`', inline=False)

        embed.add_field(name='Ping:', value='Get the latency of the bot in ms.\nExample: `ping`', inline=False)

        embed.add_field(name='Shuffle:', value='Generate randomly two teams\nExample: `shuffle <player1> <player2> <player3> <player4>`', inline=False)

        embed.add_field(name='Snowball:', value='Throw secretly a snowball on a random member or on your target.\nExample: `snowball <target?>`', inline=False)

        embed.set_image(url="https://media4.giphy.com/media/citBl9yPwnUOs/giphy.gif?cid=ecf05e47jiomict6ir7di89l00ponfmjfh98iicgan9cwwtw&rid=giphy.gif&ct=g")

        await ctx.send(embed=embed)

async def setup(client):
    await client.add_cog(Help(client))