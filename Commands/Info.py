import discord
from discord.ext import commands

class Info(commands.Cog):

    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.command()
    async def info(self, ctx, member:discord.Member=None):

        if member is None:
            member=ctx.author

        embed = discord.Embed(title=f":passport_control: Who is {member.display_name}? :identification_card:", colour=member.colour)

        embed.set_thumbnail(url=member.display_avatar),
        embed.set_footer(text=f'Requested by - {ctx.author}', icon_url=ctx.author.display_avatar)

        embed.add_field(name='Name:', value=member.display_name, inline=False),
        embed.add_field(name='Created at:', value=member.created_at, inline=False),
        embed.add_field(name='Joined at:', value=member.joined_at, inline=False),
        embed.add_field(name='Are you a bot ?', value=member.bot, inline=False),

        await ctx.send(embed=embed)

async def setup(client):
    await client.add_cog(Info(client))