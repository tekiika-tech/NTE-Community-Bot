# ======================================
# 必要な機能を読み込む
# ======================================

import sqlite3

# ======================================
# データベースへ接続
# ======================================

conn = sqlite3.connect("database/events.db")
cursor = conn.cursor()

# ======================================
# eventsテーブルを作成
# ======================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS events (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    title TEXT NOT NULL,
    genre TEXT NOT NULL,

    start_time TEXT NOT NULL,
    end_time TEXT,

    description TEXT

)
""")

# ======================================
# 保存して終了
# ======================================

conn.commit()
conn.close()

print("データベースを作成しました！")