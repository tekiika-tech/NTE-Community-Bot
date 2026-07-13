# ======================================
# 必要な機能を読み込む
# ======================================

import discord
from discord.ext import commands

from database.database import (
    add_event,
    get_events,
    delete_event,
    get_event,
)

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

# ======================================
# イベント削除プルダウン
# ======================================

class EventDeleteSelect(discord.ui.Select):

    def __init__(self):

        events = get_events()

        options = []

        for event in events:

            options.append(
                discord.SelectOption(
                    label=event[1],
                    description=event[3],
                    value=str(event[0])
                )
            )

        if not options:

            options.append(
                discord.SelectOption(
                    label="イベントがありません",
                    value="0"
                )
            )

        super().__init__(
            placeholder="削除するイベントを選択してください",
            min_values=1,
            max_values=1,
            options=options
        )

    async def callback(self, interaction: discord.Interaction):

        if self.values[0] == "0":

            await interaction.response.send_message(
                "削除できるイベントがありません。"
            )

            return

        event_id = int(self.values[0])

        event = get_event(event_id)

        delete_event(event_id)

        await interaction.response.send_message(
            f"✅ **{event[1]}** を削除しました。"
        )

# ======================================
# イベント削除View
# ======================================

class EventDeleteView(discord.ui.View):

    def __init__(self):

        super().__init__()

        self.add_item(
            EventDeleteSelect()
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

    # -----------------------------
    # /event delete
    # -----------------------------

    @discord.app_commands.command(
        name="delete",
        description="イベントを削除します"
    )
    async def delete(self, interaction: discord.Interaction):

        await interaction.response.send_message(
            "削除するイベントを選択してください。",
            view=EventDeleteView()
        )

# ======================================
# Cogを読み込む
# ======================================

async def setup(bot):

    await bot.add_cog(
        Event(bot),
        guild=discord.Object(id=1521467066001916084)
    )