import json
import os
from discord.ext import commands

with open("config.json") as f:
    data = json.load(f)
    admin = data["ADMIN_ROLE"]
    py = data["OS"]

class Reset(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Reset COg Loaded")
    
    @commands.command()
    @commands.has_any_role(admin)
    async def reset(self, ctx):
        await ctx.send("Server reset!")
        os.system(f"{py} bot.py")
        
    
def setup(client):
    client.add_cog(Reset(client))