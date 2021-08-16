import json
import os
from discord.ext import commands

with open("config.json") as f:
    data = json.load(f)
    admin = data["ADMIN_ROLE"]
    

class Reset(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Reset COg Loaded")
    
    
        
    
def setup(client):
    client.add_cog(Reset(client))