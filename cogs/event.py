import discord
from discord.ext import commands

from cogs.event_commands.create import register_create
from cogs.event_commands.list import register_list
from cogs.event_commands.delete import register_delete
from cogs.event_commands.edit import register_edit


class Event(
    commands.GroupCog,
    group_name="event"
):

    def __init__(self, bot):

        self.bot = bot


register_create(Event)
register_list(Event)
register_delete(Event)
register_edit(Event)


async def setup(bot):

    await bot.add_cog(
        Event(bot),
        guild=discord.Object(
            id=1521467066001916084
        )
    )