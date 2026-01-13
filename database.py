import sqlite3

DB_NAME = "users.db"

# 1️⃣ Connection
def get_connection():
    return sqlite3.connect(DB_NAME)

# 2️⃣ Create table + insert admin (SAFE)
def init_db():
    conn = get_connection()
    cur = conn.cursor()

    # create table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )
    """)

    # insert default admin if not exists
    cur.execute("SELECT * FROM users WHERE username='admin'")
    if not cur.fetchone():
        cur.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            ("admin", "admin123")
        )

    conn.commit()
    conn.close()

# 3️⃣ Login check
def authenticate_user(username, password):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, password)
    )

    user = cur.fetchone()
    conn.close()
    return user is not None
def save_search(username, drug):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        drug TEXT
    )
    """)
    cur.execute(
        "INSERT INTO history (username, drug) VALUES (?, ?)",
        (username, drug)
    )
    conn.commit()
    conn.close()
