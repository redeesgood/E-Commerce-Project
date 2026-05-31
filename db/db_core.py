import sqlite3
from typing import Any


class DBHelper:
    def __init__(self, db_name: str) -> None:
        self.db_name = db_name
        self.connection = sqlite3.connect(self.db_name)
        self.connection.row_factory = sqlite3.Row

    def create_tables(self) -> None:
        cursor: sqlite3.Cursor = self.connection.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT UNIQUE,
            balance INTEGER
        )               
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            item_name TEXT,
            price INTEGER,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )
        """)

        self.connection.commit()

    def execute_query(self, query: str, parametres=tuple()) -> None:
        cursor: sqlite3.Cursor = self.connection.cursor()
        cursor.execute(query, parametres)
        self.connection.commit()

    def select_all(self, query: str, parameter=tuple()) -> list[tuple[Any, ...]] | None:
        cursor: sqlite3.Cursor = self.connection.cursor()
        cursor.execute(query, parameter)
        return cursor.fetchall()

    def select_one(self, query: str, parameter=tuple()) -> tuple[Any, ...] | None:
        cursor: sqlite3.Cursor = self.connection.cursor()
        cursor.execute(query, parameter)
        return cursor.fetchone()

    def close(self) -> None:
        self.connection.close()
