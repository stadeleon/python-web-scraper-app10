import sqlite3


class Storage:
    def __init__(self, db_file_path: str):
        self.connection = sqlite3.connect(db_file_path)
        self.cursor = self.connection.cursor()

    def store(self, tour: list):
        print(tour)
        self.cursor.execute("Insert into events VALUES(Null, ?, ?, ?)", tour)

        return self.connection.commit()

    def is_tour_stored(self, tour) -> bool:
        found_row = self.cursor.execute("Select * from events where band = ? and city = ? and date = ?", tour)

        return bool(len(found_row.fetchall()))
