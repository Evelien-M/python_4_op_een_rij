import sqlite3
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "4opeenrij.db")

con = sqlite3.connect(db_path)
cur = con.cursor()

# Create table

cur.execute("CREATE TABLE IF NOT EXISTS score (id INTEGER, player VARCHAR(45) NOT NULL, time INT NOT NULL, date datetime NOT NULL, difficulty varchar(45) NOT NULL, completed tinyint(4) NOT NULL, won int(11) NOT NULL, PRIMARY KEY(id))")

cur.execute('''CREATE TABLE `game_table` (
  `id` int(11) NOT NULL,
  `x` int(11) NOT NULL,
  `y` int(11) NOT NULL,
  `value` int(11)
)''')

con.commit()

# Insert a row of data
cur.execute("INSERT INTO score VALUES (1, 'MARCO BORSATO', 10, '2021-10-11 00:00:00', 'easy', 1,1)")
cur.execute("INSERT INTO score VALUES (2, 'MARCO BORSATO', 12, '2021-10-11 00:00:00', 'easy', 0,0)")
cur.execute("INSERT INTO score VALUES (3, 'GUUS MEEUWIS', 15, '2021-10-11 00:00:00', 'easy', 1,1)")
cur.execute("INSERT INTO score VALUES (4, 'GUUS MEEUWIS', 16, '2021-10-11 00:00:00', 'hard', 1,2)")

# Save (commit) the changes
con.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
con.close()