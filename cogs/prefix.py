import json
import os
from discord.ext import commands

with open("config.json") as f:
    data = json.load(f)
    py = data["OS"]

class Prefix(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Prefix changer ready")
    
    @commands.command()
    async def prefix(self, ctx, prefix):
        with open('bot.json', 'r') as f:
                data = json.load(f)

        data["PREFIX"] = prefix

        with open("bot.json", "w") as f:
            json.dump(data, f, indent= 4)
        await ctx.send(f"Prefix changed to {prefix}")

        os.system(f"{py} bot.py")

def setup(client):
    client.add_cog(Prefix(client))   