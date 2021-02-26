import discord
from bs4 import BeautifulSoup
import requests
import asyncio
import wiki

TOKEN = 'Njc1NjI0NzA1Mzc3NDM1Njcw.Xj52ig.VrGvEqIgYnjIwKqzNLd5AQWqPEo'

client = discord.Client()

@client.event
async def on_ready():
    print('ログインしました')


@client.event
async def on_message(message):
    if message.author.bot:
        return
    elif message.content == '/AK':
        await message.channel.send("オペレーターは？")

        def check(m):
            try:
                return m.author == m.author
            except IndexError:
                return False
        
        try:
            msg = await client.wait_for('message', check=check, timeout = 10)
        except asyncio.TimeoutError:
            await message.channel.send('時間経ちすぎ！')
        
        else:
            if wiki.wiki.get_op_info(msg.content) == 1:
                await message.channel.send('情報なし')
            else:
                await message.channel.send(wiki.wiki.get_op_info(msg.content))

client.run(TOKEN)