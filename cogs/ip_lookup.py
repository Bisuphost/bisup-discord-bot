# cogs/ip_lookup.py
import discord
from discord.ext import commands
import socket
import requests

# Optional: Use ipinfo.io API for geolocation
IPINFO_TOKEN = ""  # Add your token if you have one

class IPLookup(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ip")
    async def ip_lookup(self, ctx, domain: str):
        """
        Get IP address and geolocation for a domain.
        Usage: !ip example.com
        """
        try:
            # Get IP address
            ip_address = socket.gethostbyname(domain)
            location_info = "Unknown"

            # If IPINFO_TOKEN is set, fetch geolocation
            if IPINFO_TOKEN:
                try:
                    resp = requests.get(f"https://ipinfo.io/{ip_address}/json?token={IPINFO_TOKEN}")
                    data = resp.json()
                    location_info = f"{data.get('city', '')}, {data.get('region', '')}, {data.get('country', '')}"
                except:
                    location_info = "Error fetching location"

            embed = discord.Embed(
                title=f"📍 IP Lookup: {domain}",
                color=discord.Color.purple()
            )
            embed.add_field(name="IP Address", value=ip_address, inline=False)
            embed.add_field(name="Location", value=location_info, inline=False)

            await ctx.send(embed=embed)

        except Exception as e:
            await ctx.send(f"❌ Error: {e}")

# REQUIRED for discord.py v2.x cog loading
async def setup(bot):
    await bot.add_cog(IPLookup(bot))
