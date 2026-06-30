import sqlite3

conn = sqlite3.connect("berserk.db", check_same_thread=False)
cur = conn.cursor()

def init():
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id TEXT PRIMARY KEY,
        ref TEXT,
        balance INTEGER DEFAULT 0,
        purchased INTEGER DEFAULT 0,
        rewarded INTEGER DEFAULT 0
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS subs(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        link TEXT,
        used INTEGER DEFAULT 0,
        owner TEXT
    )
    """)
    conn.commit()