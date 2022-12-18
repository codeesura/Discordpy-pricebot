
# Açıklama

``import discord`` ve ``from discord.ext import commands , tasks`` satırları, Discord API'sini kullanmak için gerekli olan kütüphaneleri içe aktarıyor.

``import requests`` satırı, HTTP istekleri yapmak için kullanılan ``requests`` kütüphanesini içe aktarıyor.

``import json`` satırı, JSON verilerini işlemek için kullanılan ``json`` kütüphanesini içe aktarıyor.

``import asyncio`` satırı, asenkron çalışma işlemleri için kullanılan ``asyncio`` kütüphanesini içe aktarıyor.

``import config`` satırı, botun API anahtarını saklamak için kullanılan ``config.py`` dosyasını içe aktarıyor.

````client = commands.Bot(command_prefix = '$')```` satırı, Discord botunun komut önekini ('$') belirler ve botu oluşturur.

````async def status_task():```` satırı, bir asenkron fonksiyon oluşturur ve bu fonksiyon, botun sunucuda gösterdiği ismin, o anda Bitcoin'in değerine göre güncellenmesini sağlar. Bu fonksiyon, sürekli çalıştırılır ve 15 saniyede bir çalıştırılır.

````try : @client.event```` satırı, bir Discord bot olayı oluşturur ve botun hazır olduğu an çalışır. Bu olay, botun sunucuda gösterdiği ismin güncellenmesi için ````status_task```` fonksiyonunu çağırır.

````client.loop.create_task(status_task())```` satırı, ``status_task`` fonksiyonunu sürekli çalıştırmaya yarar. Bu sayede, botun sunucuda gösterdiği isim sürekli güncellenir.

````print('blockland Bitocinbot hazir')```` satırı, botun hazır olduğunu gösteren bir mesaj yazdırır.

````client.run(config.BITCOIN_TOKEN)```` satırı, botun API anahtarını kullanarak botu çalıştırır. API anahtarı, ````config.py```` dosyasından içe aktarılır.
