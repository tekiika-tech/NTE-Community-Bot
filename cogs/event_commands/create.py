import discord

from database.database import add_event


class EventCreateModal(discord.ui.Modal, title="イベント作成"):

    event_name = discord.ui.TextInput(
        label="イベント名",
        required=True
    )

    genre = discord.ui.TextInput(
        label="ジャンル",
        required=True
    )

    start_time = discord.ui.TextInput(
        label="開始日時",
        placeholder="2026-07-20 20:00",
        required=True
    )

    end_time = discord.ui.TextInput(
        label="終了日時",
        placeholder="2026-07-20 22:00",
        required=False
    )

    description = discord.ui.TextInput(
        label="説明",
        style=discord.TextStyle.paragraph,
        required=False
    )

    async def on_submit(
        self,
        interaction: discord.Interaction
    ):

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


def register_create(cls):

    @discord.app_commands.command(
        name="create",
        description="イベントを登録します"
    )
    async def create(
        self,
        interaction: discord.Interaction
    ):

        await interaction.response.send_modal(
            EventCreateModal()
        )

    setattr(cls, "create", create)