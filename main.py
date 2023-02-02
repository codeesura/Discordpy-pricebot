import discord
from discord.ext import commands , tasks
import requests
import json
import asyncio
import config

client = commands.Bot(command_prefix = '$')

async def status_task():
    while True:
        try :
            getir = requests.get("https://api.dexscreener.com/latest/dex/pairs/ethereum/0x4585fe77225b41b697c938b018e2ac67ac5a20c0,0x16b9a82891338f9ba80e2d6970fdda79d1eb0dae").text
            getir = json.loads(getir)
            getir_usd = round(float(getir["pairs"][0]["priceUsd"]),0)
            await asyncio.sleep(15)
            for guild in client.guilds:
                await guild.me.edit(nick=f"${getir_usd:n}")
        except :
            continue
            
try :
    @client.event
    async def on_ready():   
        client.loop.create_task(status_task())
        print('Bot hazir!')
except :
    False

client.run(config.DISCORD_TOKEN)
