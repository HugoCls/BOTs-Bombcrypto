import discord
from discord.ext import commands, tasks

client=commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    read.start()
    print('BOT Bombcrypto is ready.')
    
@client.command()
async def clear(ctx):
    fichier=open("historic.txt", "w")
    fichier.write('$CLEARED$')
    fichier.close()
    await ctx.message.delete()
    await ctx.channel.purge(limit=100)
    await ctx.send('Cleared historic!')
  
@client.command()
async def Hello(ctx):
    await ctx.send('Heyy!')

@tasks.loop(seconds=1)
async def read():
    channel = client.get_channel(917772848968372234)
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

client.run('OTE4NTI5NTIzNTEzOTY2NjYy.YbIlRw.Qwj3k8arqTIx_g4zhNTE8YAJvT4')