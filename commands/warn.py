import discord
from discord.ext import commands
from data.checks import addWarning, is_staff
from datetime import datetime
import secrets

class Warn(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(name='warn', description='Warn a user')
    @is_staff()
    async def warn(self, ctx: discord.ApplicationContext, member: discord.Member, reason: str):
        warning = {
            "id": f"WARN-{secrets.token_hex(6)}",
            "reason": reason,
            "warned_by": ctx.author.name,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        addWarning(member.id, warning)
        
        embed = discord.Embed(
            title="`⚠️` - Warn Submitted!",
            description=f"""**`👤` - User Warned : {member.mention}**
**`🤔` - Reason : `{reason}`**
**`🛡️` - Mod That Issued Warn : {ctx.author.mention}**
**`🆔` - Warn ID : `{warning['id']}`**
**`🕒` - Time Of Warning : `{warning['date']}`**
""",
            color=discord.Color.red(),
            timestamp=discord.utils.utcnow()
        )
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(Warn(bot))