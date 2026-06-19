import discord
import random
from dotenv import load_dotenv
import os
from discord import app_commands

load_dotenv()

_BOT_TOKEN = os.getenv("BOT_TOKEN")

class PitBot(discord.Client):
    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(
            command_prefix="!",
            intents = intents
        )
        self.tree = app_commands.CommandTree(self)
    
    async def setup_hook(self):
        await self.tree.sync()

    async def on_ready(self):
        print("AAAAAAAAUUUUUUUUUHHHHH!!!!!!")

    async def on_member_join(self, member):
        canal_geral = self.get_channel(1345225581197004843)

        if canal_geral is None:
            return

        choice = random.choice([0, 1])

        if choice == 0:
            await canal_geral.send(f"""
                                   {member.mention} chegou! O Pit Bot não gostou de {member.name} <:BarreBravo:1411937476225929246>
                                   """, file=discord.File('pitbull-boxing.png'))
        else:
            await canal_geral.send(f"""
                                   {member.mention} chegou! O Pit Bot gostou de {member.name} <:mitsuojoia:1411945314994098267>\nVocê está seguro por enquanto...
                                   """, file=discord.File('pitbull-boxing.png'))
    
    async def on_member_remove(self, member):
        canal = self.get_channel(1345225581197004843)

        if canal:
            await canal.send(
                f"{member.mention} abandonou o território dos Pits..."
            )

bot = PitBot()
bot.run(_BOT_TOKEN)