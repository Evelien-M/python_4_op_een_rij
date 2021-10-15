import sqlite3
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "4opeenrij.db")

con = sqlite3.connect(db_path)
cur = con.cursor()

# Create table

cur.execute("CREATE TABLE IF NOT EXISTS score (id INTEGER, player VARCHAR(45) NOT NULL, time INT NOT NULL, date datetime NOT NULL, difficulty varchar(45) NOT NULL, width int(11) NOT NULL, height int(11) NOT NULL, status_id int(11) NOT NULL, PRIMARY KEY(id))")

cur.execute('''CREATE TABLE `game_table` (
  `id` int(11) NOT NULL,
  `x` int(11) NOT NULL,
  `y` int(11) NOT NULL,
  `value` int(11),
  `marked` tinyint(1)
)''')

cur.execute('''CREATE TABLE `game_status` (
  `id` int(11) NOT NULL,
  `name` varchar(45) NOT NULL
)''')

con.commit()

# Insert a row of data
cur.execute("INSERT INTO game_status VALUES (1, 'Speelbaar')")
cur.execute("INSERT INTO game_status VALUES (2, 'Gewonnen')")
cur.execute("INSERT INTO game_status VALUES (3, 'Verloren')")
cur.execute("INSERT INTO game_status VALUES (4, 'Gelijkspel')")

cur.execute("INSERT INTO score VALUES (1, 'MARCO BORSATO', 10, '2021-10-11 00:00:00', 'easy', 7, 6, 2)")
cur.execute("INSERT INTO score VALUES (2, 'MARCO BORSATO', 12, '2021-10-11 00:00:00', 'easy', 7, 6, 4)")
cur.execute("INSERT INTO score VALUES (3, 'GUUS MEEUWIS', 15, '2021-10-11 00:00:00', 'easy', 7, 6, 3)")
cur.execute("INSERT INTO score VALUES (4, 'GUUS MEEUWIS', 16, '2021-10-11 00:00:00', 'hard', 7, 6, 2)")

# Save (commit) the changes
con.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
con.close()