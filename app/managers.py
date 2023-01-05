import sqlite3
from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("../cinema.db3")
        self._table_name = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self._table_name} "
            f"(first_name, last_name) "
            f"VALUES (?, ?)", (first_name, last_name)
        )

    def all(self) -> [Actor]:
        cursor = self._connection.execute(
            f"SELECT * FROM {self._table_name}"
        )

        return [Actor(*row) for row in cursor]

    def update(self, id_to_update: int,
               first_name_to_update: str,
               last_name_to_update: str) -> None:

        self._connection.execute(
            f"UPDATE {self._table_name} "
            "SET (first_name, last_name) = (?, ?) "
            "WHERE id = ?",
            (first_name_to_update,
             last_name_to_update,
             id_to_update)
        )
        self._connection.commit()

    def delete(self, id_to_delete: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self._table_name} "
            "WHERE id = ?", (id_to_delete,)
        )
        self._connection.commit()
