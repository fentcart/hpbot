import discord
from discord.ext import commands

class Downloads(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="downloads")
    async def downloads(self, ctx):
        embed = discord.Embed(
            title="**iHeroic's Mods!**",
            description="""
**I Am Atomic Version: 1.3**

**Behaviour: https://link-center.net/1070006/i-am-atomic-version-13**

**Resources: https://link-target.net/1070006/i-am-atomic-13-resources**

**Elsdocia Magic Sword**

**Link : https://mcpedl.com/elsdocia-magic-sword/**

**Divine Axe Rhitta**

**Link : https://www.patreon.com/HeroicProductions/shop/divine-axe-rhitta-95828**

**Slayer Rising is currently still in production**

**Jujutsu Sorcery is currently still in production**

**If your looking for more content take a look in https://discord.com/channels/1009931397009522698/1138462698284269608 !**
""",
            color=discord.Colour.red()
        )
        embed.set_footer(text="Made By Osf0 :)")
        embed.set_thumbnail(url="https://i.imgur.com/k2oL6gt.png")
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(Downloads(bot))
