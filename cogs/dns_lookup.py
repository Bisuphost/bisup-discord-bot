# cogs/dns_lookup.py
import discord
from discord.ext import commands
import dns.resolver

class DNSLookup(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="dns")
    async def dns_lookup(self, ctx, domain: str):
        """
        Lookup DNS records for a domain.
        Usage: !dns example.com
        """
        try:
            result = {}

            # Get A records (IP addresses)
            try:
                a_records = dns.resolver.resolve(domain, "A")
                result["A"] = [r.to_text() for r in a_records]
            except:
                result["A"] = ["No A records found"]

            # Get NS records (nameservers)
            try:
                ns_records = dns.resolver.resolve(domain, "NS")
                result["NS"] = [r.to_text() for r in ns_records]
            except:
                result["NS"] = ["No NS records found"]

            # Get MX records (mail servers)
            try:
                mx_records = dns.resolver.resolve(domain, "MX")
                result["MX"] = [r.to_text() for r in mx_records]
            except:
                result["MX"] = ["No MX records found"]

            # Build embed
            embed = discord.Embed(
                title=f"🔍 DNS Lookup: {domain}",
                color=discord.Color.green()
            )
            for record_type, values in result.items():
                embed.add_field(
                    name=record_type,
                    value="\n".join(values),
                    inline=False
                )

            await ctx.send(embed=embed)

        except Exception as e:
            await ctx.send(f"❌ Error: {e}")

# REQUIRED for cog loading in discord.py v2.x
async def setup(bot):
    await bot.add_cog(DNSLookup(bot))
