import discord

from database.database import get_events


def register_list(cls):

    @discord.app_commands.command(
        name="list",
        description="登録済みイベントを表示します"
    )
    async def list(
        self,
        interaction: discord.Interaction
    ):

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

    setattr(cls, "list", list)