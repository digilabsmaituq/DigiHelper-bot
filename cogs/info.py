import json
import os
import discord
from discord.ext import commands

with open('user.json', 'r') as f:
    data = json.load(f)

ceo = data["CEO"]
coo = data["COO"]
cfo = data["CFO"]

class Info(commands.Cog):
    def __init__(self, client):
       self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Info Cog ready")
    
    @commands.command()
    async def info(self, ctx):
        
        embed=discord.Embed(title="About Digilab", description="An IT community based on Ummul Quro Bogor Islamic High School. This is a place where students from Ummul Quro High School could improve or learn new IT skills.")
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/865094112725303346/865094478360870942/digilab_logo2.png?width=462&height=462")
        embed.add_field(name="CEO", value=ceo, inline=True)
        embed.add_field(name="CFO", value=cfo, inline=True)
        embed.add_field(name="COO", value=coo, inline=True)
        embed.set_footer(text="DIgilab 2021/2020")

        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Info(client))