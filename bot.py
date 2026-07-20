import asyncio
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

from database.init_db import init_database

load_dotenv()

TOKEN = os.getenv("TOKEN")
GUILD_ID = int(os.getenv("GUILD_ID"))

intents = discord.Intents.default()

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)


@bot.event
async def on_ready():

    guild = discord.Object(id=GUILD_ID)

    synced = await bot.tree.sync(
        guild=guild
    )

    print(f"{len(synced)}個のコマンドを同期しました！")
    print(f"{bot.user} がオンラインになりました！")


async def main():

    init_database()

    async with bot:

        await bot.load_extension("cogs.ping")
        await bot.load_extension("cogs.event")

        await bot.start(TOKEN)


asyncio.run(main())