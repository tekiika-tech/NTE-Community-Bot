# ======================================
# 必要な機能を読み込む
# ======================================

import discord
from discord.ext import commands

# ======================================
# /event グループ
# ======================================

event = discord.app_commands.Group(
    name="event",
    description="イベント機能"
)

# ======================================
# Event機能
# ======================================

class Event(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @event.command(
        name="create",
        description="イベントを作成します"
    )
    async def create(
        self,
        interaction: discord.Interaction
    ):

        await interaction.response.send_message(
            "イベントを作成します！"
        )

# ======================================
# Cogを読み込む
# ======================================

async def setup(bot):

    cog = Event(bot)

    await bot.add_cog(cog)

    bot.tree.add_command(event)