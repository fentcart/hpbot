import discord
from discord.ext import commands
from datetime import datetime
from data.checks import getWarnings, removeWarning, is_staff

async def warn_id_autocomplete(ctx: discord.AutocompleteContext):
    user_id = ctx.options.get('user')
    if user_id:
        warnings = getWarnings(user_id)
        return [f"ID: {warning['id']} - Reason: {warning['reason']} - Date: {warning['date']}" for warning in warnings]
    return []

class RemoveWarn(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='removewarn', description='Remove a warning by ID')
    @is_staff()
    async def removewarn(
        self,
        ctx: discord.ApplicationContext,
        user: discord.User,
        warn_id: discord.Option(
            str,
            description="Select a warning ID to remove",
            required=True,
            autocomplete=warn_id_autocomplete
        ) # type: ignore
    ):
        warn_id = warn_id.split(" - ")[0].replace("ID: ", "")
        
        removeWarning(user.id, warn_id)
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        embed = discord.Embed(
            title="`🛡️` - Warning Removed!",
            description=f"**User : <@{user.id}>**\n**`🆔` - Warn ID : `{warn_id}`**\n**`🕒` - Time Of Removal : `{date}`**\n**`🛡️` - Removed By : {ctx.author.mention}**",
            color=discord.Color.red(),
            timestamp=datetime.utcnow()
        )
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(RemoveWarn(bot))