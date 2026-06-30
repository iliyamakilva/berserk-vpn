from db import cur, conn
from config import REF_REWARD

def reward_ref(user_id):
    cur.execute("SELECT ref, rewarded FROM users WHERE id=?", (user_id,))
    row = cur.fetchone()

    if not row:
        return

    ref, rewarded = row

    if ref and rewarded == 0:
        cur.execute("UPDATE users SET balance = balance + ? WHERE id=?",
                    (REF_REWARD, ref))
        cur.execute("UPDATE users SET rewarded=1 WHERE id=?",
                    (user_id,))
        conn.commit()