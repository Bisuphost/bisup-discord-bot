import discord
from discord.ext import commands
import os
import requests
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    print("⚠️ GEMINI_API_KEY is not set!")

class AIHelper(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        # Predefined system context for the AI
        self.context = (
            "You are BisupHelper, an AI assistant specialized in web hosting, domains, "
            "servers, and related technical topics. Only answer questions related to these topics. "
            "If a user asks something unrelated, politely say: '⚠️ I can only answer questions about web hosting, domains, and servers.' "
            "Bisup is a web hosting company."
        )

    @commands.command(name="ask")
    async def ask(self, ctx, *, query: str):
        """Ask Gemini AI a question."""
        await ctx.send("🤖 Thinking...")

        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"
        headers = {"Content-Type": "application/json"}
        data = {
            "contents": [
                {"parts": [{"text": f"{self.context}\n\nUser question: {query}"}]}
            ]
        }

        try:
            response = requests.post(url, headers=headers, json=data)
            if response.ok:
                reply = response.json()["candidates"][0]["content"]["parts"][0]["text"]
                await ctx.send(reply[:2000])
            else:
                await ctx.send(f"⚠️ Gemini API Error {response.status_code}: {response.text}")
        except Exception as e:
            await ctx.send(f"❌ Request failed: {e}")

async def setup(bot):
    await bot.add_cog(AIHelper(bot))
