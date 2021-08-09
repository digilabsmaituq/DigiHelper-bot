import json
import discord
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
    async def help(self, ctx):
        author = ctx.message.author

        embed = discord.Embed(colour = discord.Color.blue())

        embed.set_author(name="Digilab")
        embed.add_field(name='Information', value="This is content")

        await ctx.send(author, embed=embed)

def setup(client):
    client.add_cog(Help(client))