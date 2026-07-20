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


# ======================================
# イベント一覧を取得
# ======================================

def get_events():

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            id,
            title,
            genre,
            start_time,
            end_time,
            description
        FROM events
        ORDER BY start_time ASC
    """)

    events = cursor.fetchall()

    conn.close()

    return events


# ======================================
# イベントを1件取得
# ======================================

def get_event(event_id: int):

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            id,
            title,
            genre,
            start_time,
            end_time,
            description
        FROM events
        WHERE id = ?
    """, (event_id,))

    event = cursor.fetchone()

    conn.close()

    return event


# ======================================
# イベントを削除
# ======================================

def delete_event(event_id: int):

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM events
        WHERE id = ?
    """, (event_id,))

    conn.commit()
    conn.close()


# ======================================
# イベントを更新
# ======================================

def update_event(
    event_id: int,
    title: str,
    genre: str,
    start_time: str,
    end_time: str,
    description: str
):

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE events
        SET
            title = ?,
            genre = ?,
            start_time = ?,
            end_time = ?,
            description = ?
        WHERE id = ?
    """, (
        title,
        genre,
        start_time,
        end_time,
        description,
        event_id
    ))

    conn.commit()
    conn.close()