
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

# Kurulum

Discord token'ınızı oluşturmak için Discord Developer Portal'ını ziyaret etmelisiniz. Bu portal, Discord botlarınızı oluşturmanız için gerekli olan token ve diğer bilgileri sağlar. Aşağıdaki adımları takip ederek Discord token'ınızı oluşturabilirsiniz:

Discord Developer Portal'ına gidin ve üye olun veya giriş yapın.
https://discord.com/developers/applications

Sol menüde "Applications" (Uygulamalar) sekmesine tıklayın.
"New Application" (Yeni Uygulama) butonuna tıklayın ve uygulamanız için bir isim verin.
![image](https://user-images.githubusercontent.com/120671243/208293307-ebb80bc7-667e-4232-8291-58d493fd357f.png)

"Create" (Oluştur) butonuna tıklayın ve uygulamanız oluşturun.

![image](https://user-images.githubusercontent.com/120671243/208293343-9aec62fb-a148-43d2-93cc-dfbe558451d5.png)

![image](https://user-images.githubusercontent.com/120671243/208293418-ace472c6-ea9b-4523-ba2e-0a0bacb3d226.png)

Add Bot'a tıklayıp botunuzu oluşturun
![image](https://user-images.githubusercontent.com/120671243/208293445-91565c9e-a284-4fed-afe5-6ba5ef92c383.png)

"Reset token" (Yeni bir token oluştur) sekmesine tıklayın ve bir token oluşturun.
Token'ınızı bir kere oluşturulduğunda, "Copy" (Kopyala) butonuna tıklayarak token'ınızı kopyalayabilir ve token'ınızı güvenli bir yerde saklayabilirsiniz.
![image](https://user-images.githubusercontent.com/120671243/208293471-cbea2248-d58d-4749-a2a9-2cd1160a9f3e.png)

Discord token oluşturduktan sonra aşağıdaki kodu girip repoyu bilgisayarınıza ekleyin ;

```
git clone https://github.com/codeesura/Discordpy-pricebot
```

ardından gerekli kütüphaneleri indirelim ;

```
pip install -r requirements.txt
```

Kütüphaneler de indikten sonra ``config.py`` dosyasındaki ``DISCORD_TOKEN`` "YOUR_TOKEN" kısmına kendi tokeninizi yazıp kaydedin. 

