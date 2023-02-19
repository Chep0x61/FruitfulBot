import os
import random
import praw
import discord
from discord.ext import commands


class Meme(commands.Cog):

    def __init__(self, client: commands.Bot):
        self.client = client

        r_id = os.getenv('r_id')
        r_secret = os.getenv('r_secret')
        r_username = os.getenv('r_username')
        r_pwd = os.getenv('r_pwd')
        r_uagent = os.getenv('r_uagent')
        self.reddit = praw.Reddit(client_id=r_id, client_secret=r_secret, username=r_username, password=r_pwd,
                                  user_agent=r_uagent)

    @commands.command()
    async def meme(self, ctx: commands.Context):
        subreddit_list = ["FrenchMemes", "HistoryMemes", "meme", "memes", "ProgrammerHumor"]
        subreddit = self.reddit.subreddit(random.choice(subreddit_list))

        all_submis = []
        top = subreddit.top(limit=10)
        for submission in top:
            all_submis.append(submission)
        sub = random.choice(all_submis)
        title = sub.title
        pic = sub.url

        embed = discord.Embed(title=title, color=discord.Colour.from_rgb(255, 69, 0))
        embed.set_image(url=pic)
        embed.set_footer(text="r/{}".format(subreddit), icon_url=subreddit.icon_img)

        await ctx.message.delete()
        await ctx.send(embed=embed)

async def setup(client):
    await client.add_cog(Meme(client))