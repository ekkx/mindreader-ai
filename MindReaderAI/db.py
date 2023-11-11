import sqlite3


class DB:
    def __init__(self, db_path: str) -> None:
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS posts (
                id INTEGER PRIMARY KEY
            )
            """
        )
        self.conn.commit()

    def queue(self, post_id: int) -> None:
        self.cursor.execute(f"INSERT INTO posts (id) VALUES ({post_id})")
        self.conn.commit()

    def is_queued(self, post_id: int) -> bool:
        self.cursor.execute(f"SELECT * FROM posts WHERE id = ({post_id})")
        return True if self.cursor.fetchone() else False

    def has_new(self, posts: list) -> bool:
        self.cursor.execute(
            f"SELECT id FROM posts WHERE id IN ({', '.join(map(str, [post.id for post in posts]))})"
        )
        return not bool(self.cursor.fetchall())

    def fetch_all(self) -> list:
        self.cursor.execute("SELECT id FROM posts")
        result = self.cursor.fetchall()
        return [row[0] for row in result]
