import discord
from discord import app_commands
import asyncio
import PySimpleGUI as sgui
from enum import Enum
from Logs import LoggingSystem

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
        eventLogCanvas = sgui.Canvas(background_color="#000", size=(600, 600), expand_x = True, expand_y = True)
        self.add_to_layout_vertical([eventLogCanvas])

        
        self.add_to_layout(sgui.Button("Shut Down", size = (10, 2)), rowIndex=2)
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
        print(self.windowLayout)
        self.window = sgui.Window(title="yClient for Discord", layout = self.windowLayout, margins=(100, 50))
        event, values = self.window.read()
        return event, values
