import config
from discord.ext import commands
import discord

# client = discord.Client()
# @client.event
# async def on_ready():
#     print('Bot is now online and ready to listen')


bot = commands.Bot(command_prefix='!')
bot.remove_command('help')  # this line is necessary to ensure that the default 
                            # help command is overwritten
                            
@bot.event
async def on_ready():
    print('Ready')                            

@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title = 'Bot Commands',
        description = 'Welcome to the help section',
        color = discord.Color.red()
    )
    
    embed.set_thumbnail(url='https://i.guim.co.uk/img/media/dd703cd39013271a45bc199fae6aa1ddad72faaf/0_0_2000_1200/master/2000.jpg?width=1200&height=1200&quality=85&auto=format&fit=crop&s=178a9434c272d5a067353f57a30f58ed')
    
    embed.add_field(
        name = '!help',
        value = 'List all of the commands',
        inline = True
    )
    
    embed.add_field(
        name = '!punch',
        value = 'P  unches another player',
        inline = True
    )
    
    embed.add_field(
        name = '!roundhouse_kick',
        value = 'Kicks another player',
        inline = True
    )
    
    await ctx.send(embed = embed)

@bot.command() 
async def punch(ctx, arg): # arg is the term that comes after the command
    """ 
        This command punches another player
    """
    
    await ctx.send(f'Punched {arg}')

    
@bot.command()
async def roundhouse_kick(ctx, *args):
    everyone = ''.join(args)
    
    
    await ctx.send(f'Roundhouse kicked {everyone}')


key = config.Discord_bot_key
# client.run(key)
bot.run(key)