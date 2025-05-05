# init_db.py

import sqlite3
import os

os.makedirs("data", exist_ok=True)
conn = sqlite3.connect("data/users.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    quiz_score INTEGER DEFAULT 0,
    support_count INTEGER DEFAULT 0
)
""")

conn.commit()
conn.close()
print("✅ Banco de dados criado com sucesso!")
