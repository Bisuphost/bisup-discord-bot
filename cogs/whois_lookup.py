# cogs/whois_lookup.py
import discord
from discord.ext import commands
import whois

class WhoisLookup(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="domain")
    async def domain_lookup(self, ctx, domain: str):
        """
        Lookup WHOIS info for a domain.
        Usage: !domain example.com
        """
        try:
            w = whois.whois(domain)

            # Format some key info
            registrar = w.registrar or "Unknown"
            creation = w.creation_date or "Unknown"
            expiry = w.expiration_date or "Unknown"

            # Build an embed for nicer display
            embed = discord.Embed(
                title=f"🌐 WHOIS Lookup: {domain}",
                color=discord.Color.blue()
            )
            embed.add_field(name="Registrar", value=str(registrar), inline=False)
            embed.add_field(name="Creation Date", value=str(creation), inline=True)
            embed.add_field(name="Expiry Date", value=str(expiry), inline=True)

            await ctx.send(embed=embed)

        except Exception as e:
            await ctx.send(f"❌ Error: {e}")

async def setup(bot):
    await bot.add_cog(WhoisLookup(bot))
