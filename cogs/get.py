import json
from discord.ext import commands
from discord.ext.commands.core import command

with open("config.json") as f:
    data = json.load(f)
    admin = data["ADMIN_ROLE"]

class GetData(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self, ctx):
        print("GetData cog ready")
    
    @commands.command()
    @commands.has_any_role(admin)
    async def getjson(self, ctx):
        with open("bot.json", "r") as f:
            data = json.load(f)
        await ctx.send(f"```\n{data}\n```")
    
def setup(client):
    client.add_cog(GetData(client))