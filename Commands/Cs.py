import discord
from discord.ext import commands

class SimpleView(discord.ui.View):

    def __init__(self, ip: str):
        super().__init__()
        self.ip = ip

    @discord.ui.button(label="Copy to Clipboard", style=discord.ButtonStyle.success)

    async def hello(self, interaction: discord.Interaction, button: discord.ui.Button):
        #pyperclip.copy(self.ip)
        await interaction.response.send_message("IP Copied !")

class Cs(commands.Cog):

    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.command()
    async def cs(self, ctx, ip: str):

        embed = discord.Embed(title=f"{ctx.author.name} is on a server!", description="Join him before there are no more slots left.\n\n**connect {}**".format(ip), colour=ctx.author.colour)

        embed.set_thumbnail(url=ctx.author.display_avatar)

        view = SimpleView(ip)
        await ctx.send(embed=embed)
        await ctx.send(view=view)




async def setup(client):
    await client.add_cog(Cs(client))