import json
import os
from discord.ext import commands
from discord.ext.commands.core import command

with open("config.json") as f:
    data = json.load(f)
    admin = data["ADMIN_ROLE"]
    py = data["OS"]

class Devtools(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Devtools ready")
    
    @commands.command()
    @commands.has_any_role(admin)
    async def getjson(self, ctx):
        with open("bot.json", "r") as f:
            data = json.load(f)
        await ctx.send(f"```json\n{json.dumps(data, indent=2)}\n```")
    
    @commands.command()
    @commands.has_any_role(admin)
    async def getmember(self, ctx):
        with open("member.json", "r") as f:
            data = json.load(f)
        await ctx.send(f"```json\n{json.dumps(data, indent=1)}\n```")
    
    @commands.command()
    @commands.has_any_role(admin)
    async def resetmember(self, ctx):
        data = json.load(open('member.json'))
        
        data = dict()

        with open('member.json', 'w') as f:
            json.dump(data, f)
        
        await ctx.send(f'data has successfully reset!')
    
    @commands.command()
    @commands.has_any_role(admin)
    async def reset(self, ctx):
        await ctx.send("Server reset!")
        os.system(f"{py} bot.py")

def setup(client):
    client.add_cog(Devtools(client))