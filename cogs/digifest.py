import json
import discord
from discord.ext import commands

with open("bot.json") as f:
    data = json.load(f)
    year = data["DIGIFEST"]["YEAR"]
    desc = data["DIGIFEST"]["DESC"]
    img = data["DIGIFEST"]["IMG"]

class Digifest(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("DIGIFEST 2021 Ready")
 
    @commands.command()
    async def digifest(self, ctx):
        embed = discord.Embed(title=f"DIGIFEST {year}", description=desc, color=0x00d1e0)
        embed.set_image(url=img)
        await ctx.send(embed = embed)

def setup(client):
    client.add_cog(Digifest(client))
