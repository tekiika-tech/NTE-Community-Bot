import discord
from discord.ext import commands


class Ping(commands.Cog):
    """ /ping コマンド """

    def __init__(self, bot):
        self.bot = bot

    @discord.app_commands.command(
        name="ping",
        description="Botが正常に動作しているか確認します"
    )
    async def ping(self, interaction: discord.Interaction):

        await interaction.response.send_message("NTE Community Botは正常に動作中です")


async def setup(bot):
    await bot.add_cog(Ping(bot))