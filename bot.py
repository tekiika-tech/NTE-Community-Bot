# ======================================
# 必要な機能を読み込む
# ======================================

import os                              # .envを使う
import discord                         # Discordの機能
from discord.ext import commands       # Botの基本機能
from dotenv import load_dotenv         # .envを読み込む

# ======================================
# .envを読み込む
# ======================================

load_dotenv()

# .envからTOKENを取得
TOKEN = os.getenv("TOKEN")

# ★開発用サーバーID
GUILD_ID = 1521467066001916084

# ======================================
# Botの設定
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

    # ★開発用サーバーだけにコマンドを登録
    guild = discord.Object(id=GUILD_ID)
    bot.tree.copy_global_to(guild=guild)

    synced = await bot.tree.sync(guild=guild)

    print(f"{len(synced)}個のコマンドを同期しました！")
    print(f"{bot.user} がオンラインになりました！")

# ======================================
# /ping コマンド
# ======================================

@bot.tree.command(
    name="ping",
    description="Botが正常に動作しているか確認します"
)
async def ping(interaction: discord.Interaction):

    await interaction.response.send_message("Pong!")

# ======================================
# Bot起動
# ======================================

bot.run(TOKEN)