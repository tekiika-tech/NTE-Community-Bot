# ======================================
# 必要な機能を読み込む
# ======================================

import sqlite3

# ======================================
# データベース設定
# ======================================

DATABASE = "database/events.db"

# ======================================
# イベントを追加
# ======================================

def add_event(
    title: str,
    genre: str,
    start_time: str,
    end_time: str,
    description: str
):

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO events (
            title,
            genre,
            start_time,
            end_time,
            description
        )
        VALUES (?, ?, ?, ?, ?)
    """, (
        title,
        genre,
        start_time,
        end_time,
        description
    ))

    conn.commit()
    conn.close()