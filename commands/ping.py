import discord
from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="ping", description="Get The Ping Of The Bot!")
    async def ping(self, ctx):
        latency = self.bot.latency
        ping = round(latency*1000)
        embed = discord.Embed(title="Bot Ping!",description=f"**Pong! :ping_pong:**\n\n**🌏 Bot Ping : `{ping}`**\n**📶 Raw Latency : `{latency}`**", color=discord.Colour.red())
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(Ping(bot))
