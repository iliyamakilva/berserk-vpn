import sqlite3

conn = sqlite3.connect("berserk.db", check_same_thread=False)
cur = conn.cursor()

def init():
    cur.execute('''CREATE TABLE IF NOT EXISTS users (
        id TEXT PRIMARY KEY,
        balance INTEGER DEFAULT 0,
        ref_code TEXT,
        invited_by TEXT,
        purchase_done INTEGER DEFAULT 0,
        reward_given INTEGER DEFAULT 0
    )''')

    cur.execute('''CREATE TABLE IF NOT EXISTS subs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        link TEXT,
        status TEXT DEFAULT 'free',
        owner TEXT
    )''')

    cur.execute('''CREATE TABLE IF NOT EXISTS logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user TEXT,
        action TEXT,
        data TEXT
    )''')

    conn.commit()

def log(user, action, data=""):
    cur.execute("INSERT INTO logs (user, action, data) VALUES (?,?,?)",
                (user, action, data))
    conn.commit()
