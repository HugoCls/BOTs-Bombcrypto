import discord
from discord.ext import commands, tasks
from itertools import cycle
import os
import asyncio
client=commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    read.start()
    pict_historic.start()
    print('BOT is running.')
    
@client.command()
async def clear(ctx):
    fichier=open("historic.txt", "w")
    fichier.write('$CLEARED$')
    fichier.close()
    await ctx.channel.purge(limit=100)
    await ctx.send('Cleared historic!')
  
@client.command()
async def Hello(ctx):
    await ctx.send('Heyy!')

@client.command()
async def picture(ctx):
        await ctx.channel.send(file=discord.File(os.getcwd()+'\img.png'))
            
@tasks.loop(seconds=5)
async def read():
    channel = client.get_channel(917460520754372648)
    fichier=open("historic.txt", "r")
    txt=fichier.read()
    fichier.close()
    if len(txt)==0:
        fichier=open("historic.txt", "a")
        fichier.write('$')
        fichier.close()
        
    if len(txt)>=1:
        if txt[0]!='$':
            fichier=open("historic.txt", "w")
            L1 = list(txt)
            L2=['$']
            for i in range(len(L1)):
                L2.append(L1[i])
            txt = ''.join(str(e) for e in L2)
            fichier.write(txt)
            fichier.close()
        fichier=open("historic.txt", "a")
        l=len(txt)-1
        if txt[l]!='$':
            j=l
            while txt[j]!='$':
                j-=1
            text_to_send=txt[j+1:len(txt)]
            if len(text_to_send)<=100:
                await channel.send(text_to_send)
            fichier.write('$')
        fichier.close()
@tasks.loop(seconds=300)
async def pict_historic():
    channel = client.get_channel(917772745549414400)
    #await channel.purge(limit=100)
    await channel.send(file=discord.File(os.getcwd()+'\screenshot.png'))
    #await asyncio.sleep(1)
    messages = messages = await channel.history(limit=200).flatten()
    #print(messages)
    for message in messages:
        await message.add_reaction('\U0001F44D')

client.run('OTE3MTY0NTMwNTgzMzU1NDUy.Ya0uCA.MR-4i6IiM-7Bui8GBJs_GeWhqqg')