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
    description="イベント管理"
)

# ======================================
# Event機能
# ======================================

class Event(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # -----------------------------
    # /event create
    # -----------------------------
    @event.command(
        name="create",
        description="イベントを登録します"
    )
    async def create(
        self,
        interaction: discord.Interaction
    ):

        await interaction.response.send_message(
            "イベント作成モーダルを開きます！（開発中）",
            ephemeral=True
        )

# ======================================
# Cogを読み込む
# ======================================

async def setup(bot):

    cog = Event(bot)

    await bot.add_cog(cog)

    try:
        bot.tree.add_command(event)
    except discord.app_commands.CommandAlreadyRegistered:
        pass