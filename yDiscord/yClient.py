import discord
from discord import app_commands
import asyncio

class Client(discord.Client):
    tree = None
    guildID = 1030675232245174393 #Your GUILD ID (Set to None to be able to use cmds everywhere - it takes an hour for commands to be registered if set to None)

    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(intents=intents)

    def def_cmds(self):
        self.tree = app_commands.CommandTree(self)

        @self.tree.command(name='hi', description='Just saying hi!', guild=discord.Object(id=self.guildID))
        async def hi(interaction):
            await interaction.response.send_message("Hi")

    async def on_ready(self):
        self.def_cmds()
        await self.tree.sync(guild=discord.Object(id=self.guildID))
        print(f"Logged on as {self.user}!")
        await self.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Murine Cops - Cuphead OST"))

#To run...
# client = Client()
# client.run(TOKENSTR)