import discord
from discord.ext import commands

class SuggestionModal(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(
            discord.ui.InputText(
                label="Suggestion",
                placeholder="Whats Your Suggestion?",
                style=discord.InputTextStyle.paragraph
            ),
            title="Heroic Productions"
        )

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.defer()

        channel = self.bot.get_channel(1230696682606297139)
        embed = discord.Embed(
            title="We Have A New Suggestion!",
            description=f"""
**Suggestion Made By : {interaction.user.mention}**

**Suggestion : `{self.children[0].value}`**

""",
            color=discord.Colour.red(),
            timestamp=discord.utils.utcnow()
        )
        message = await channel.send(embed=embed)
        await message.add_reaction('👍')
        await message.add_reaction('👎')

        user = interaction.user
        await user.create_dm()
        embeddm = discord.Embed(title="Thanks For Sending A Suggestion Through!", color=discord.Colour.red(), timestamp=discord.utils.utcnow())
        await user.send(embed=embeddm)

class Suggestion(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="suggestion", description="Create A Suggestion")
    async def suggestion(self, ctx):
        modal = SuggestionModal(title="Heroic Productions")
        await ctx.send_modal(modal=modal)

def setup(bot):
    bot.add_cog(Suggestion(bot))
