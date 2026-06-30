from db import cur, conn

def get_free_sub():
    cur.execute("SELECT id, link FROM subs WHERE status='free' LIMIT 1")
    return cur.fetchone()

def assign_sub(sub_id, user_id):
    cur.execute("UPDATE subs SET status='used', owner=? WHERE id=?",
                (user_id, sub_id))
    conn.commit()
