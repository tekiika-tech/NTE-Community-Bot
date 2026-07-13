import discord
from discord.ext import commands
from database.database import add_event,get_events,delete_event,get_event

class EventCreateModal(discord.ui.Modal,title="イベント作成"):
    event_name=discord.ui.TextInput(label="イベント名",required=True)
    genre=discord.ui.TextInput(label="ジャンル",required=True)
    start_time=discord.ui.TextInput(label="開始日時",required=True)
    end_time=discord.ui.TextInput(label="終了日時",required=False)
    description=discord.ui.TextInput(label="説明",style=discord.TextStyle.paragraph,required=False)
    async def on_submit(self,interaction):
        add_event(title=str(self.event_name),genre=str(self.genre),start_time=str(self.start_time),end_time=str(self.end_time),description=str(self.description))
        await interaction.response.send_message("✅ イベントを登録しました！")

class EventDeleteSelect(discord.ui.Select):
    def __init__(self):
        ev=get_events()
        opts=[discord.SelectOption(label=e[1],description=e[3],value=str(e[0])) for e in ev] or [discord.SelectOption(label="イベントがありません",value="0")]
        super().__init__(placeholder="削除するイベントを選択してください",options=opts)
    async def callback(self,interaction):
        if self.values[0]=="0":
            await interaction.response.send_message("削除できるイベントがありません。");return
        eid=int(self.values[0]);e=get_event(eid);delete_event(eid)
        await interaction.response.send_message(f"✅ **{e[1]}** を削除しました。")

class EventDeleteView(discord.ui.View):
    def __init__(self):
        super().__init__();self.add_item(EventDeleteSelect())

class Event(commands.GroupCog,group_name="event",group_description="イベント管理"):
    def __init__(self,bot): self.bot=bot
    @discord.app_commands.command(name="create")
    async def create(self,interaction): await interaction.response.send_modal(EventCreateModal())
    @discord.app_commands.command(name="list")
    async def list(self,interaction):
        ev=get_events()
        if not ev:
            await interaction.response.send_message("📭 登録されているイベントはありません。");return
        embed=discord.Embed(title="📅 登録済みイベント",color=discord.Color.blue())
        for e in ev:
            embed.add_field(name=f"{e[0]}. {e[1]}",value=f"**ジャンル**：{e[2]}\n**開始日時**：{e[3]}\n**終了日時**：{e[4] or '未設定'}\n**説明**：{e[5] or 'なし'}",inline=False)
        await interaction.response.send_message(embed=embed)
    @discord.app_commands.command(name="delete")
    async def delete(self,interaction):
        await interaction.response.send_message("削除するイベントを選択してください。",view=EventDeleteView())

async def setup(bot):
    await bot.add_cog(Event(bot),guild=discord.Object(id=1521467066001916084))
