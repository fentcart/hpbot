import discord
from discord.ext import commands
from data.checks import is_staff
from typing import Literal

class WarnRequest(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @discord.slash_command(name="requestmodaction", description="Command For Trail Mods To Report A Action!")
    @is_staff()
    async def requestmodaction(
        self, 
        ctx: discord.ApplicationContext, 
        user: discord.Member, 
        action_type: str,
        reason: str, 
        screenshot: discord.Attachment
    ):
        if action_type not in ['ban', 'warn', 'kick', 'mute']:
            await ctx.respond("Invalid action type. Please use one of the following: 'ban', 'warn', 'kick', 'mute'.", ephemeral=True)
            return

        await ctx.defer()
        channel = self.bot.get_channel(1263076580222046218)
        message = "@Admins"
        embed = discord.Embed(
            title="`🛡️` - Mod Action Requested By Trail Admin!",
            description=f"""
**`🛡️` - Mod That Issued Request : {ctx.author.mention}**
**`👤` - User Being Reported : `{user.name} ({user.id})`**
**`🛡️` - Type Of Action Being Issued : `{action_type}`**
**`🤔` - Reason For The Issue : `{reason}`**

`Proof Below :`
""",
            color=discord.Color.red(),
            timestamp=discord.utils.utcnow()
        )
        embed.set_image(url=screenshot.url)

        view = RequestActionView(ctx.author, user, action_type, reason)

        await channel.send(content=message, embed=embed, view=view)
        await ctx.respond("Your Report Has Been Submitted You Will Be DM'd With The Update On Your Request!", ephemeral=True)


class RequestActionView(discord.ui.View):
    def __init__(self, requester, user, action_type, reason):
        super().__init__(timeout=None)
        self.requester = requester
        self.user = user
        self.action_type = action_type
        self.reason = reason

    @discord.ui.button(label="Confirm", style=discord.ButtonStyle.green)
    async def confirm_button(self, button: discord.ui.Button, interaction: discord.Interaction):
        await self.handle_decision(interaction, confirmed=True)

    @discord.ui.button(label="Decline", style=discord.ButtonStyle.red)
    async def decline_button(self, button: discord.ui.Button, interaction: discord.Interaction):
        await self.handle_decision(interaction, confirmed=False)

    async def handle_decision(self, interaction: discord.Interaction, confirmed: bool):
        for child in self.children:
            child.disabled = True
        await interaction.response.edit_message(view=self)
        decision = "Confirmed" if confirmed else "Declined"
        adminmsg = discord.Embed(
            title=f"`🛡️` - You `{decision}` {self.requester} Action To {self.action_type} {self.user}",
            color=discord.Color.red(),
            timestamp=discord.utils.utcnow() 
        )

        admin2msg = discord.Embed(
            title=f"`🛡️` - Your Action To {self.action_type} {self.user} Has Been `{decision}`",
            color=discord.Color.red(),
            timestamp=discord.utils.utcnow() 
        )

        if confirmed != False:
            message = "Please Take Action On The User!"

        await self.requester.send(embed=admin2msg)

        await interaction.user.send(embed=adminmsg)
        await interaction.user.send(message)


def setup(bot):
    bot.add_cog(WarnRequest(bot))