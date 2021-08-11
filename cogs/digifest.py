import json
from discord.ext import commands

with open("digifest.json") as f:
    data = json.load(f)
    year = data["DIGIFEST"]["YEAR"]
    desc = data["DIGIFEST"]["DESC"]

class Digifest(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("DIGIFEST 2021 Ready")

    @commands.command()
    async def digifest(self, ctx):
        await ctx.send(f"Welcome to DIGIFEST {year}!")

def setup(client):
    client.add_cog(Digifest(client))
