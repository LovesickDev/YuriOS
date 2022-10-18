import discord

class Client(discord.Client):
    def __init__(self) -> None:
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(intents=intents)

    async def run_client(self, tkn) -> None:
        
        self.run(tkn)
    
    async def on_ready(self):
        print(f"Logged on as {self.user}!")