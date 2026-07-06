# ======================================
# 必要な機能を読み込む
# ======================================

import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# ======================================
# .envを読み込む
# ======================================

load_dotenv()

TOKEN = os.getenv("TOKEN")

# 開発用サーバーID
GUILD_ID = 1521467066001916084

# ======================================
# Bot設定
# ======================================

intents = discord.Intents.default()

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)

# ======================================
# Bot起動時
# ======================================

@bot.event
async def on_ready():

    guild = discord.Object(id=GUILD_ID)

    synced = await bot.tree.sync(guild=guild)

    print(f"{len(synced)}個のコマンドを同期しました！")
    print(f"{bot.user} がオンラインになりました！")


# ======================================
# 起動時の準備
# ======================================

async def main():

    async with bot:

        # ★ cogsフォルダのping.pyを読み込む
        await bot.load_extension("cogs.ping")

        # ★ コマンドを同期

        await bot.start(TOKEN)


# ======================================
# Bot起動
# ======================================

import asyncio

asyncio.run(main())