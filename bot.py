# bot.py
import discord
from discord.ext import commands
import os
import config

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")
    await bot.change_presence(activity=discord.Game(name="!help for commands"))

async def load_cogs():
    """Load all extensions (cogs)"""
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")

async def main():
    async with bot:
        await load_cogs()
        await bot.start(config.DISCORD_TOKEN)

# Run bot properly
import asyncio
asyncio.run(main())
