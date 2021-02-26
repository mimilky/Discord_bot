import discord
import Riot
import asyncio
from riotwatcher import LolWatcher, ApiError

TOKEN = 'TOKEN'

client = discord.Client()

@client.event
async def on_ready():
    print('ログインしました')

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == '/lol':
        await message.channel.send('サモナーネームは？')
        
        def chack(m):
            try:
                return m.author == m.author
            except IndexError:
                return False
    
        try :
            msg = await client.wait_for('message', check=chack, timeout = 10)
            
        except asyncio.TimeoutError:
            await message.channel.send('時間経ちすぎ！')

        #サモナー情報なしのとき0, ランク情報なしのとき1 
        else:
            if Riot.rank(msg.content) == 0:
                await message.channel.send('そんな奴いない！')
            elif Riot.rank(msg.content) == 1:
                await message.channel.send('こいつランクやってない！')
            else:
                await message.channel.send('ランク:' + Riot.rank(msg.content)['tier'] + Riot.rank(msg.content)['rank'])
        


client.run(TOKEN)
