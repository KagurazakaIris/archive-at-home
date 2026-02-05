import os
import aiosqlite

# 获取当前文件所在目录的上一级目录 (client/)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "client_data.db")


async def init_db():
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            """
            CREATE TABLE IF NOT EXISTS resolve_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                gid TEXT NOT NULL,
                token TEXT NOT NULL,
                username TEXT,
                gp_cost INTEGER,
                download_url TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """
        )
        await db.commit()


async def add_record(gid, token, username, gp_cost, download_url):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            """
            INSERT INTO resolve_history (gid, token, username, gp_cost, download_url)
            VALUES (?, ?, ?, ?, ?)
        """,
            (str(gid), str(token), username, gp_cost, download_url),
        )
        await db.commit()
