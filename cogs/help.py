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
        embed=discord.Embed(title="Command List", description="List of commands that you can use with this bot. To see the use case of each command, add 'help' in the end of each command.", color=0x00d1e0)

        embed.set_author(name="DigiHelper Bot", url="https://github.com/digilabsmaituq/DigiHelper-bot")
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/865094112725303346/865094478360870942/digilab_logo2.png?width=462&height=462")
        embed.add_field(name="d!help", value="Showing this list.", inline=False)
        embed.add_field(name="d!admin", value="List of admin tools. This command only can be used by any role that has Administrator permission.", inline=False)
        embed.set_footer(text="Digilab 2021/2022")

        await ctx.send(embed=embed)
    
    @commands.command()
    @commands.has_any_role(admin)
    async def admin(self, ctx):
        embed=discord.Embed(title="Admin Tools", description="Admin only tools.", color=0x00d1e0)

        embed.set_author(name="DigiHelper Bot", url="https://github.com/digilabsmaituq/DigiHelper-bot")
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/865094112725303346/865094478360870942/digilab_logo2.png?width=462&height=462")
        embed.add_field(name="d!insert", value="Adding a new CEO name to the database.", inline=False)
        embed.set_footer(text="Digilab 2021/2022")

        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Help(client))