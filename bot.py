import discord
import json
import os
from discord.ext import commands, tasks
from itertools import cycle
status = cycle(['DIGIFEST 2021', 'Use d!help for more information'])

with open('config.json') as f:
    data = json.load(f)
    token = data["TOKEN"]
    prefix = data["PREFIX"]

client = commands.Bot(command_prefix=prefix, help_command=None)

@client.event
async def on_ready():
    change_status.start()
    print('Bot running')

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Invalid command')

@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(token)
