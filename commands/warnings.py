import discord
from discord.ext import commands
from data.checks import getWarnings, is_staff
from datetime import datetime

class Warnings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(name='warnings', description='Show warnings of a user')
    @is_staff()
    async def warnings(self, ctx: discord.ApplicationContext, member: discord.Member):
        warnings = getWarnings(member.id)
        embed = discord.Embed(
            title=f'`⚠️` - Warnings for `{member.name}`',
            color=discord.Color.red(),
            timestamp=datetime.utcnow()
        )
        
        if warnings:
            embed.description = f'**`⚠️` - {member.mention} has `{len(warnings)}` warning(s):**'
            for index, warn in enumerate(warnings, start=1):
                embed.add_field(
                    name=f'**{index}.**',
                    value=f'**`🤔` - Reason: `{warn["reason"]}`**\n**`🛡️` - Warned by: `{warn["warned_by"]}`**\n**`🕒` - Date: `{warn["date"]}`**\n**`🆔` - Warning ID: `{warn["id"]}`**',
                    inline=False
                )
        else:
            embed.description = f'**`⚠️` - {member.mention} has no warnings.**'

        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(Warnings(bot))
