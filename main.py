import disnake as discord

from disnake.ext import commands
from os import listdir

intents = discord.Intents.default()
intents.message_content = True

bot = commands.InteractionBot(intents=intents)

@bot.event
async def on_ready():
    print(f"Bot online.")

def load_cogs(bot):
    for filename in listdir("./cogs"):
        if filename.endswith(".py"):
            bot.load_extension(f"cogs.{filename[:-3]}")

if __name__ == "__main__":
    load_cogs(bot)
    bot.run("MTEzNzMzMTUzNDI1NzQ1OTI4MQ.Gz9bV6.WEEAzf0JMq-_dk5gmeZpPIA2brj_9sFyz6sFvA")