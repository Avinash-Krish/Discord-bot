import discord
import os

client = discord.Client()


@client.event
async def on_ready():
    print('Online')
    
    
@client.event
async def on_message(message):    
    
    if message.author == client.user: 
        return 
    
    if message.content == 'haha':
        await message.add_reaction('\U0001F602')
    
        
@client.event
async def on_message_edit(before, after):   
    await before.channel.send(
        f"{before.author} edited a message \n"
        f"Original message: {before.content}\n"
        f"Edited message: {after.content}\n"        
        )
    
    
@client.event
async def on_reaction_add(reaction, user):
    await reaction.message.channel.send(f"{user} reacted with {reaction.emoji}")
    


#NOTE: this token isn't made public just like Djano's secret key
