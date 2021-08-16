import json
from discord.ext import commands
from discord.ext.commands.core import command

with open("config.json") as f:
    data = json.load(f)
    admin = data["ADMIN_ROLE"]

class Member(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Members Cog Ready")

    @commands.command()
    async def register(self, ctx, *, name):
        data = json.load(open('member.json'))

        if type(data) is dict:
            data = [data]
        
        data.append({
            "Member": name
        })

        with open('member.json', 'w') as f:
            json.dump(data, f)
        
        await ctx.send(f'{name} has successfully registered!')

def setup(client):
    client.add_cog(Member(client))
