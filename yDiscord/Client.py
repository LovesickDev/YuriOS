import discord
from discord import app_commands
from discord.ext import commands
import asyncio
import PySimpleGUI as sgui
from enum import Enum
#from Logs import LoggingSystem

#TODO tree has cmds but it isnt showing up on discord for some reason

class Client(discord.Client):
    guildID = 1055368762796290079 #Your GUILD ID (Set to None to be able to use cmds everywhere - it takes an hour for commands to be registered if set to None)

    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)
    
    def setup_cmd_tree(self):

        @self.tree.command(name="hi", description="Greetings!")
        async def hi(ctx):
            ctx.send("Hello!!")
        

    async def on_ready(self):
        self.setup_cmd_tree()
        await self.tree.sync(guild=self.get_guild(self.guildID))
        print(f"Logged on as {self.user}!")
        await self.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Murine Cops - Cuphead OST"))
        print(self.tree.get_commands())
#To run...
# client = Client()
# client.run(TOKENSTR)

class ClientUIEvents(Enum):
    EXIT = 0

class ClientUI():

    window = None
    windowLayout = []

    def __init__(self):
        self.create_UI()
        return
    
    def create_UI(self):
        menu_def = [
            ["Client", ["Change Client Token", "Change DEBUG Channel ID"]],
            ["Window", ["Change Theme"]],
            ["Help", "About YuriOS"]        
                    ]
        menu = sgui.Menu(menu_def)
        self.add_to_layout_vertical([menu])

        self.add_to_layout_vertical([sgui.Text("Welcome to yClient User Interface.")])
        
        #Event Log
        eventLog = sgui.Output(background_color="#000", size=(10, 20), expand_x = True, expand_y = True)
        self.add_to_layout_vertical([eventLog])

        
        self.add_to_layout_vertical([sgui.Button("Shut Down", size = (10, 2))])
        return
    
    def add_to_layout_vertical(self, items, index=None):
        if index is None:
            self.windowLayout.append(items)
        else:
            self.windowLayout.insert(index, items)
        return

    def add_to_layout(self, items, columnIndex=None, rowIndex=None):
        if rowIndex is None:
            if columnIndex is None:
                self.windowLayout[len(self.windowLayout) - 1].append(items)
            else:
                self.windowLayout[len(self.windowLayout) - 1].insert(columnIndex, items)
        else:
            if columnIndex is None:
                self.windowLayout[rowIndex].append(items)
            else:
                self.windowLayout[rowIndex].insert(columnIndex, items)
        
        return

    def monitor_event(self, event):
        if event == "Shut Down" or event == sgui.WIN_CLOSED:
            return ClientUIEvents.EXIT

    def run(self):
        self.window = sgui.Window(title="yClient for Discord", layout = self.windowLayout, margins=(100, 50))
        event, values = self.window.read()
        return event, values
