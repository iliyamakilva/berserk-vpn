from db import cur, conn

def handle_ref(user_id, ref):
    if not ref:
        return
    if str(user_id) == str(ref):
        return

    cur.execute("INSERT OR IGNORE INTO users (id, invited_by) VALUES (?,?)",
                (user_id, ref))
    conn.commit()
