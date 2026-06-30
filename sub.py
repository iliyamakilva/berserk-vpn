from db import cur, conn

def get_sub():
    cur.execute("SELECT * FROM subs WHERE used=0 LIMIT 1")
    return cur.fetchone()


def assign_sub(sub_id, user_id):
    cur.execute("UPDATE subs SET used=1, owner=? WHERE id=?",
                (user_id, sub_id))
    conn.commit()