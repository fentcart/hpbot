import discord
from discord.ext import commands

class ServerInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="serverinfo", description="get server info")
    async def serverinfo(self, ctx):
        server = self.bot.get_guild(1009931397009522698)
        embed = discord.Embed(
            title="Heroic Productions Server Info",
            description=f"""
**Member Count : `{server.member_count}`**
**Channel Count : `{len(server.channels)}`**
**Categorie Count : `{len(server.categories)}`**
""",
            color=discord.Colour.red()
        )
        embed.set_image(url="https://i.imgur.com/k2oL6gt.png")
        embed.set_footer(text="Made By Osf0 :)", icon_url="https://i.imgur.com/k2oL6gt.png")
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(ServerInfo(bot))
