from yDiscord import yClient
from yDiscord.yClient import ClientUIEvents

class yuriOS: #old stuff change later
    discordBot = None

    def __init__(self) -> None:
        print("Module Initialized.")
        pass

    def run_discord(self, tkn) -> None:

        self.discordBot = yClient.Client()
        self.discordBot.run(tkn)


#UI STUFF
ui = yClient.ClientUI()

while True: #ui loop example
    event, values = ui.run()
    #you need to manage the events within whatever loop you want to use
    if ui.monitor_event(event) == ClientUIEvents.EXIT:
        print("Putting the window out of its misery x-x..")
        break

ui.window.close()