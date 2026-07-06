# ======================================
# 必要な機能を読み込む
# ======================================

import discord
from discord.ext import commands

# ======================================
# Event機能
# ======================================

class Event(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # /event コマンド
    @discord.app_commands.command(
        name="event",
        description="イベント機能"
    )
    async def event(self, interaction: discord.Interaction):

        await interaction.response.send_message(
            "イベント機能は現在開発中です！"
        )

# ======================================
# Cogを読み込む
# ======================================

async def setup(bot):
    await bot.add_cog(Event(bot))