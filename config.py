import os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()  # Loads .env file

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")