# ======================================
# 必要な機能を読み込む
# ======================================

import sqlite3

# ======================================
# データベース設定
# ======================================

DATABASE = "database/events.db"

# ======================================
# データベース初期化
# ======================================

def init_database():

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

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

    conn.commit()
    conn.close()

# ======================================
# メイン処理
# ======================================

if __name__ == "__main__":

    init_database()

    print("データベースを作成しました！")