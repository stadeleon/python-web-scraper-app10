import sqlite3

connection = sqlite3.connect("../databases/scrappy.db")
cursor = connection.cursor()

# result = cursor.execute("DELETE from events where id=0")
# result = cursor.execute("Select * from events where true")
#
# print(result.fetchall())

new_rows = [('Camels', 'Tiger City', '2088.10.16', None),
            ('Elephants', 'Elephants City', '2048.10.31', None)]

# cursor.executemany("Insert into events VALUES(?, ?, ?, ?)", new_rows)
connection.commit()
result = cursor.execute("Select * from events")
print(result.fetchall())
