import discord

from database.database import (
    get_events,
    get_event,
    update_event
)


class EventEditModal(discord.ui.Modal):

    def __init__(self, event):

        super().__init__(title="イベント編集")

        self.event = event

        self.title_input = discord.ui.TextInput(
            label="イベント名",
            default=event[1],
            required=True
        )

        self.genre_input = discord.ui.TextInput(
            label="ジャンル",
            default=event[2],
            required=True
        )

        self.start_input = discord.ui.TextInput(
            label="開始日時",
            default=event[3],
            required=True
        )

        self.end_input = discord.ui.TextInput(
            label="終了日時",
            default=event[4] or "",
            required=False
        )

        self.description_input = discord.ui.TextInput(
            label="説明",
            default=event[5] or "",
            style=discord.TextStyle.paragraph,
            required=False
        )

        self.add_item(self.title_input)
        self.add_item(self.genre_input)
        self.add_item(self.start_input)
        self.add_item(self.end_input)
        self.add_item(self.description_input)

    async def on_submit(
        self,
        interaction: discord.Interaction
    ):

        update_event(
            event_id=self.event[0],
            title=str(self.title_input),
            genre=str(self.genre_input),
            start_time=str(self.start_input),
            end_time=str(self.end_input),
            description=str(self.description_input)
        )

        await interaction.response.send_message(
            f"✅ **{self.title_input}** を更新しました。"
        )


class EventEditSelect(discord.ui.Select):

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

            placeholder="編集するイベントを選択してください",

            min_values=1,
            max_values=1,

            options=options

        )

    async def callback(
        self,
        interaction: discord.Interaction
    ):

        if self.values[0] == "0":

            await interaction.response.send_message(
                "編集できるイベントがありません。"
            )

            return

        event = get_event(
            int(self.values[0])
        )

        await interaction.response.send_modal(
            EventEditModal(event)
        )


class EventEditView(discord.ui.View):

    def __init__(self):

        super().__init__()

        self.add_item(
            EventEditSelect()
        )


def register_edit(cls):

    @discord.app_commands.command(
        name="edit",
        description="イベントを編集します"
    )
    async def edit(
        self,
        interaction: discord.Interaction
    ):

        await interaction.response.send_message(
            "編集するイベントを選択してください。",
            view=EventEditView(),
            ephemeral=True
        )

    setattr(cls, "edit", edit)