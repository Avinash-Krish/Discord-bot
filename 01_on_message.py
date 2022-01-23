import discord
import os

client = discord.Client() # this client object is used to connect to the discord web socket and API

"""
In discord, if someone sends a message or reacts is called an event. Using our bot, we can listen to those events
"""

@client.event
async def on_ready(): # this function is part of discord packeage and is triggered when the bot is online and is ready to listen
    print('Bot is now online and ready to listen')
    
@client.event
async def on_message(message):    
    
    if message.author == client.user: # cheking if the bot has sent the message and then breaking out of the loop so that an infinite loop of the bot texting itself doesn't happen
        return 
    
    if message.content == 'hello':
        await message.channel.send('Welcome to the channel')
    
    # await message.channel.send('Hey there!') # making sure that the bot sends the response in the same channel(discord) and not in a different channel

#NOTE: Below is the way to hide the key which didn't work. Maybe enabling a virtual environment might make it work
# key = os.environ.get('Discord_bot_key')
# print(key)    
# client.run(key)
# the parameter that is being passed is the token that authorizes the bot to run


#NOTE: this token isn't made public just like Djano's secret key
