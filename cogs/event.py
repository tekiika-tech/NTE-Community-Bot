# ======================================
# 必要な機能を読み込む
# ======================================

import discord
from discord.ext import commands

from database.database import add_event, get_events

# ======================================
# イベント作成モーダル
# ======================================

class EventCreateModal(discord.ui.Modal, title="イベント作成"):

    # -----------------------------
    # 入力項目
    # -----------------------------

    event_name = discord.ui.TextInput(
        label="イベント名",
        placeholder="例：ワールドボス",
        required=True,
        max_length=100
    )

    genre = discord.ui.TextInput(
        label="ジャンル",
        placeholder="例：ワールドイベント",
        required=True,
        max_length=100
    )

    start_time = discord.ui.TextInput(
        label="開始日時",
        placeholder="例：2026-07-10 20:00",
        required=True,
        max_length=30
    )

    end_time = discord.ui.TextInput(
        label="終了日時",
        placeholder="例：2026-07-10 21:00",
        required=False,
        max_length=30
    )

    description = discord.ui.TextInput(
        label="説明",
        style=discord.TextStyle.paragraph,
        required=False,
        max_length=1000
    )

    # -----------------------------
    # モーダル送信
    # -----------------------------

    async def on_submit(self, interaction: discord.Interaction):

        add_event(
            title=str(self.event_name),
            genre=str(self.genre),
            start_time=str(self.start_time),
            end_time=str(self.end_time),
            description=str(self.description)
        )

        await interaction.response.send_message(
            "✅ イベントを登録しました！"
        )

# ======================================
# Event機能
# ======================================

class Event(
    commands.GroupCog,
    group_name="event",
    group_description="イベント管理"
):

    def __init__(self, bot):
        self.bot = bot

    # -----------------------------
    # /event create
    # -----------------------------

    @discord.app_commands.command(
        name="create",
        description="イベントを登録します"
    )
    async def create(self, interaction: discord.Interaction):

        await interaction.response.send_modal(
            EventCreateModal()
        )

    # -----------------------------
    # /event list
    # -----------------------------

    @discord.app_commands.command(
        name="list",
        description="登録済みイベントを表示します"
    )
    async def list(self, interaction: discord.Interaction):

        events = get_events()

        if not events:

            await interaction.response.send_message(
                "📭 登録されているイベントはありません。"
            )

            return

        embed = discord.Embed(
            title="📅 登録済みイベント",
            color=discord.Color.blue()
        )

        for event in events:

            embed.add_field(
                name=f"{event[0]}. {event[1]}",
                value=(
                    f"**ジャンル**：{event[2]}\n"
                    f"**開始日時**：{event[3]}\n"
                    f"**終了日時**：{event[4] or '未設定'}\n"
                    f"**説明**：{event[5] or 'なし'}"
                ),
                inline=False
            )

        await interaction.response.send_message(
            embed=embed
        )

# ======================================
# Cogを読み込む
# ======================================

async def setup(bot):

    await bot.add_cog(
        Event(bot),
        guild=discord.Object(id=1521467066001916084)
    )