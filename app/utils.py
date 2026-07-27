import random
import string
import sqlite3

DATABASE_NAME = "data.db"

HOST = "127.0.0.1"
PORT = 8000

def generate_short_code(lenght: int = 8) -> str:
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=lenght))

def url_exist(url):
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row

    row = conn.execute("SELECT short_code FROM links WHERE original_url = ?", (url,)).fetchone()
    conn.close()

    return row


def create_link(code: str) -> str:
    return f"http://{HOST}:{PORT}/{code}"