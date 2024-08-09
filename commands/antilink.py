from datetime import datetime
import re
import secrets
import discord
import asyncio
from discord.ext import commands
from data.checks import addWarning

class AntiLink(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.allowed_roles = [1009943383785078836, 1136451117610446848, 1213694663983108106]
        self.allowed_gif_hosts = [
            "giphy.com",
            "tenor.com",
            "gyfcat.com",
            "imgur.com",
            "youtube.com",
            "spotify.com",
            "roblox.com",
            "discord.com"
        ]

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        if any(role.id in self.allowed_roles for role in message.author.roles):
            return

        url_pattern = re.compile(r'(https?://[^\s]+)')
        if url_pattern.search(message.content):
            if not self.is_allowed_gif(message.content):
                warning = {
                    "id": f"WARN-{secrets.token_hex(6)}",
                    "reason": "Link in general (AUTO)",
                    "warned_by": "Heroic Productions Auto-MOD",
                    "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                addWarning(message.author.id, warning)
                await message.delete()
                date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                embed = discord.Embed(
                    title="`🔗` - Anti-Link Found A Message!",
                    description=f"""
    **`🛡️` - {message.author.mention}, You Are Not Allowed To Send Links!**
    **`🕒` - Time Of Warning : `{warning['date']}`**
    """,
                    color=discord.Color.red(),
                    timestamp=discord.utils.utcnow()
                )
                msg = await message.channel.send(embed=embed)
                await asyncio.sleep(5)
                await msg.delete()

    def is_allowed_gif(self, content):
        return any(host in content for host in self.allowed_gif_hosts)

def setup(bot):
    bot.add_cog(AntiLink(bot))