import discord
from discord.ext import commands

class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(1064931344972517396)
        embed = discord.Embed(
            title="Welcome!",
            description=f"**Welcome {member.mention}!, To `Heroic Productions` We Hope You Have A Wonderful Time In Here And Have Fun!**\n\n**DOWNLOADS : https://discord.com/channels/1009931397009522698/1196289405921533986**",
            color=discord.Colour.red()
        )
        embed.set_thumbnail(url=member.avatar.url if member.avatar else member.default_avatar.url)
        embed.set_footer(text="Made By Osf0 :)")
        await channel.send(embed=embed)

def setup(bot):
    bot.add_cog(Welcome(bot))