import config
from discord.ext import commands

# client = discord.Client()
# @client.event
# async def on_ready():
#     print('Bot is now online and ready to listen')


bot = commands.Bot(command_prefix='!')

@bot.command() 
async def punch(ctx, arg): # arg is the term that comes after the command
    """ 
        !punch Justin
        Justin is the arg
    """
    
    await ctx.send(f'Punched {arg}')

# this decorator looks for the function name followed by the '!'
# then triggers the function once the message is received
@bot.command() 
async def info(ctx): # the name of the function is the name of the command
    """
        ctx - context object that contains information on how the command was executed
        
        !info is the command
    """

    await ctx.send(ctx.guild)
    await ctx.send(ctx.author)
    await ctx.send(ctx.message.id)
    
@bot.command()
async def roundhouse_kick(ctx, *args):
    everyone = ''.join(args)
    """
        !roundhouse_kick is the command
    """
    
    await ctx.send(f'Roundhouse kicked {everyone}')


key = config.Discord_bot_key
# client.run(key)
bot.run(key)