import disnake as discord

from cogs.ticket import *
from cogs.verify import *
from disnake.ext import commands
from os import listdir

intents = discord.Intents.default()
intents.message_content = True

bot = commands.InteractionBot(intents=intents)
@bot.event
async def on_ready(persistent_view_added=None):
    if not persistent_view_added:
        bot.add_view(ticketButtons())
        bot.add_view(verifyButton())
        persistent_view_added = True


def load_cogs(bot):
    for filename in listdir("./cogs"):
        if filename.endswith(".py"):
            bot.load_extension(f"cogs.{filename[:-3]}")

if __name__ == "__main__":
    load_cogs(bot)
    bot.run("MTEzNzMzMTUzNDI1NzQ1OTI4MQ.Gz9bV6.WEEAzf0JMq-_dk5gmeZpPIA2brj_9sFyz6sFvA")