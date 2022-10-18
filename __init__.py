from .yDiscord import yClient

class yuriOS:
    discordBot = None

    def __init__(self) -> None:
        print("Module Initialized.")
        pass

    def run_discord(self, tkn) -> None:

        self.discordBot = yClient.Client()
        self.discordBot.run(tkn)