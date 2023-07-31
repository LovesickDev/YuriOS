from yDiscord import Client
from yDiscord.Client import ClientUIEvents
import asyncio
import threading
import Logs

class yuriOS:
    async_loop = None

    discordBot = None
    discordTkn = None
    ui = None

    def __init__(self) -> None:
        tknfile = open('./../discord.txt', 'r')
        self.discordBot = Client.Client()
        self.discordTkn = tknfile.read()
        #print(self.discordTkn)
        pass

    def run_discord(self) -> None:
        Logs.LoggingSystem.log("connect")
        self.discordBot.run(self.discordTkn)

    async def stop_discord(self) -> None:
        await self.discordBot.close()
        self.discordBot = None
    
    async def update_ui(self) -> None:
        print("2")
        self.ui = Client.ClientUI()

        while True: #ui loop example
            await asyncio.sleep(0.1)
            event, values = self.ui.run()
            #you need to manage the events within whatever loop you want to use
            if self.ui.monitor_event(event) == ClientUIEvents.EXIT:
                print("Putting the window out of its misery x-x..")
                break
            
        self.ui.window.close()

    async def run_ui(self):
            await asyncio.gather(self.update_ui())
    
    def run(self):
        discordbot_thread = threading.Thread(target=self.run_discord)
        discordbot_thread.start()

        asyncio.run(self.run_ui())

_yos = yuriOS()
_yos.run()