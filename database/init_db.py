# ======================================
# 必要な機能を読み込む
# ======================================

import sqlite3

# ======================================
# データベースへ接続
# ======================================

# events.db が無ければ自動で作成される
conn = sqlite3.connect("database/events.db")

# SQLを実行するための準備
cursor = conn.cursor()

# ======================================
# eventsテーブルを作成
# ======================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS events (

    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    start_date TEXT NOT NULL,
    end_date TEXT NOT NULL,
    description TEXT

)
""")

# ======================================
# 保存して終了
# ======================================

conn.commit()
conn.close()

print("データベースを作成しました！")