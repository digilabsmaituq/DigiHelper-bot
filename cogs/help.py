import json
from discord.ext import commands

with open('config.json') as f:
    data = json.load(f)
    admin = data["ADMIN_ROLE"]

class Help(commands.Cog):
    def __init__(self, client):
       self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Help Cog ready")
    
    @commands.command()
    @commands.has_any_role(admin)
    async def help(self, ctx):
        await ctx.send('This command is for help')

def setup(client):
    client.add_cog(Help(client))