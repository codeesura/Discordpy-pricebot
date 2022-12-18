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
            getir = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true&include_last_updated_at=true").text
            getir = json.loads(getir)
            getir_usd = int(getir["bitcoin"]["usd"])
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
