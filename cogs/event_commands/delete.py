import discord

from database.database import (
    get_events,
    get_event,
    delete_event
)


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

    async def callback(
        self,
        interaction: discord.Interaction
    ):

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


class EventDeleteView(discord.ui.View):

    def __init__(self):

        super().__init__()

        self.add_item(
            EventDeleteSelect()
        )


def register_delete(cls):

    @discord.app_commands.command(
        name="delete",
        description="イベントを削除します"
    )
    async def delete(
        self,
        interaction: discord.Interaction
    ):

        await interaction.response.send_message(
            "削除するイベントを選択してください。",
            view=EventDeleteView(),
            ephemeral=True
        )

    setattr(cls, "delete", delete)