import random
import discord
from discord.ext import commands

class Shuffle(commands.Cog):

    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.command()
    async def shuffle(self, ctx, *members):

        if len(members) < 4 or len(members) > 50 or len(members) % 2 != 0:
            print('nope')
            return
        print(members)
        arguments = list(members)
        print(arguments)
        for i in range(3):
            random.shuffle(arguments)
        print(arguments)
        team_size = len(arguments) // 2
        team1 = arguments[:team_size]
        team2 = arguments[team_size:]

        embed = discord.Embed(title=f"Team Generator {team_size}vs{team_size}")

        embed.set_footer(text=f'Shuffle requested by - {ctx.author}', icon_url=ctx.author.display_avatar)

        team1_field = ""
        for player in team1:
            team1_field += f"**{player}**\n"
        embed.add_field(name='Team #1:', value=team1_field, inline=True)

        team2_field = ""
        for player in team2:
            team2_field += f"**{player}**\n"
        embed.add_field(name='Team #2:', value=team2_field, inline=True)

        embed.set_image(url="https://media1.giphy.com/media/l2Je30ZHMjidHGHLO/giphy.gif?cid=ecf05e47txn2mdkdx987skkyzphcng3zk4mlxmc3e04kgt56&rid=giphy.gif&ct=g")

        await ctx.send(embed=embed)
        await ctx.send(f"Equipe 1 : {', '.join(team1)}\nEquipe 2 : {', '.join(team2)}")

async def setup(client):
    await client.add_cog(Shuffle(client))