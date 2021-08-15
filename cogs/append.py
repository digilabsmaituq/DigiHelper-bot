import json
import os
from discord.ext import commands

with open('config.json') as f:
    data = json.load(f)
    admin = data["ADMIN_ROLE"]
    py = data["OS"]

    
class Add(commands.Cog):
    def __init__(self, client):
       self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("insert Cog ready")

    @commands.command()
    @commands.has_any_role(admin)
    async def insert(self, ctx, args, *,name:str):
        with open('bot.json', 'r') as f:
            data = json.load(f)

        if args == "ceo":
            data["CORE"]["CEO"] = name

        if args == "coo":
            data["CORE"]["COO"] = name

        if args == "cfo":
            data["CORE"]["CFO"] = name

        with open("bot.json", "w") as f:
            json.dump(data, f, indent= 4)

        await ctx.send("Added")
        
        os.system(f"{py} bot.py")

    @commands.command()
    @commands.has_any_role(admin)
    async def inserthelp(self, ctx):
        await ctx.send("Command for adding the CEO, COO, and CFO name to the database.\nUse case:\n```d!insert <ceo/coo/cfo> <name>```")

def setup(client):
    client.add_cog(Add(client))
