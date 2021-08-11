import json
import os
import discord
from discord.ext import commands

with open('config.json') as f:
    data = json.load(f)
    admin = data["ADMIN_ROLE"]

class Add(commands.Cog):
    def __init__(self, client):
       self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("insert Cog ready")

    @commands.command()
    @commands.has_any_role(admin)
    async def insert(self, ctx, args, *,name:str):
        if args == "ceo":
            with open('user.json', 'r') as f:
                data = json.load(f)

            data["CEO"] = name

            with open("user.json", "w") as f:
                json.dump(data, f, indent= 4)
            await ctx.send("Added")

        if args == "coo":
            with open('user.json', 'r') as f:
                data = json.load(f)

            data["COO"] = name

            with open("user.json", "w") as f:
                json.dump(data, f, indent= 4)
            await ctx.send("Added")

        if args == "cfo":
            with open('user.json', 'r') as f:
                data = json.load(f)

            data["CFO"] = name

            with open("user.json", "w") as f:
                json.dump(data, f, indent= 4)
            await ctx.send("Added")

        os.system('python3 bot.py')

    @commands.command()
    @commands.has_any_role(admin)
    async def inserthelp(self, ctx):
        await ctx.send("Command for adding the CEO, COO, and CFO name to the database.\nUse case:\n```d!insert <ceo/coo/cfo> <name>```")

def setup(client):
    client.add_cog(Add(client))
