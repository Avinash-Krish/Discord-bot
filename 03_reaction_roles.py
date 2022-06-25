import discord
import config

intents = discord.Intents.default()
intents.members = True

#NOTE: intents are groups of events in discord and one of those is member intents


class MyClient(discord.Client): # our own class that inherits from the parent class discord.Client
    
    def __init__(self, *args, **kwargs):
        super().__init__() # super is a reference to the parent class
        #NOTE: super().__init__(*args, **kwargs) - this didn't work even though the tutorial said that we have to pass the args and kwargs
        # here, super() initialises the discord.Client() class
        self.target_message_id = 934709666448031764
        
    async def on_ready(self):
        print('Ready')
        
        
    async def on_raw_reaction_add(self, payload):
        """
            This method assigns a role based on the reaction emoji
        """
        if payload.message_id != self.target_message_id:
            return 

        #NOTE: each server is called a guild; a bot can run on multiple servers
        
        guild = client.get_guild(payload.guild_id)
        
        #NOTE: utils is a discord library that has the 'get' function and this function takes two arguments,
        # an iterable and attributes. Here, we are running through the roles in the guild and assigning the role if the emoji matches
        
        if payload.emoji.name == '🥔':
            role = discord.utils.get(guild.roles, name = 'potato person')
            await payload.member.add_roles(role)
        elif payload.emoji.name == '💩':
            role = discord.utils.get(guild.roles, name = 'chocolate person')
            await payload.member.add_roles(role)
        elif payload.emoji.name == '🐵':
            role = discord.utils.get(guild.roles, name = 'funky monkey')
            await payload.member.add_roles(role)
        
    async def on_raw_reaction_remove(self, payload): 
        """
            This method removes a role based on the reaction emoji
        """
        
        if payload.message_id != self.target_message_id:
            return 
        
        guild = client.get_guild(payload.guild_id)
        member = guild.get_member(payload.user_id) # removing the role for the user that is deleting the reaction
        
        
        if payload.emoji.name == '🥔':
            role = discord.utils.get(guild.roles, name = 'potato person')
            await member.remove_roles(role)
        elif payload.emoji.name == '💩':
            role = discord.utils.get(guild.roles, name = 'chocolate person')
            await member.remove_roles(role)
        elif payload.emoji.name == '🐵':
            role = discord.utils.get(guild.roles, name = 'funky monkey')
            await member.remove_roles(role)


client = MyClient(intents)
key = config.Discord_bot_key
client.run(key)
