import sqlite3
import os.path
import model
import datetime
import random
from model.Score import Score
from model.Table import Content, Table

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "4opeenrij.db")


def getHighscoreHomepage():
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    list = []
    for r in cur.execute('SELECT * FROM score WHERE status_id = 2 ORDER BY time ASC LIMIT 10'):
        score = Score(r[0],r[1],r[2],r[3],r[4],r[5])
        list.append(score)
    
    con.close()
    return list


def createGame(name,difficulty):
    try:
        con = sqlite3.connect(db_path)
        cur = con.cursor()
        cur.execute("INSERT INTO score VALUES (NULL, '"+ str(name) +"', 0, '"+ str(datetime.datetime.now()) +"', '"+ str(difficulty) +"', 1)")
        id = cur.lastrowid
        for x in range(7): 
            for y in range(6):
                cur.execute("INSERT INTO game_table VALUES (" + str(id) + ", "+ str(x) +", "+ str(y) +", 0,0)")

        # add random oponent turn 
        r = random.randrange(0, 2)
        if r == 1:
            column = random.randrange(0,7)
            cur.execute("INSERT INTO game_table VALUES (" + str(id) + ", "+ str(column) +", "+ str(5) +", 2,0)")

        con.commit()
        con.close()
        return id
    except Exception as e: 
        print(str(e))
        return None


def getGame(id):
    try:
        con = sqlite3.connect(db_path)
        cur = con.cursor()
        list = Table()
        for r in cur.execute('SELECT * FROM game_table WHERE id = '+ str(id)):
            list.Table[r[2]][r[1]] = Content(r[3],r[4])
            
        con.close()
        return list
    except Exception as e:
        print(str(e))


def getScore(id):
    try:
        con = sqlite3.connect(db_path)
        cur = con.cursor()
        
        for r in cur.execute('SELECT * FROM score WHERE id = '+ str(id) + ' LIMIT 1'):
            score = Score(id,r[1],r[2],r[3],r[4],r[5])
            status = ""
            for r in cur.execute('SELECT * FROM game_status WHERE id = '+ str(score.status) + ' LIMIT 1'):
                status = r[1]
            score.statusName = status

        con.close()
        return score
    except Exception as e:
        print(str(e))


def updateGame(id,table):
    try:
        con = sqlite3.connect(db_path)
        cur = con.cursor()
        for x in range(7): 
            for y in range(6):
                cur.execute('UPDATE game_table SET value=' + str(table.Table[y][x].value) + ', marked=' + str(table.Table[y][x].marked) + ' WHERE id = '+ str(id) +' AND x =' + str(x) + ' AND y =' + str(y))

        con.commit()  
        con.close()
    except Exception as e:
        print(str(e))

def updateScore(score):
    try:
        con = sqlite3.connect(db_path)
        cur = con.cursor()
        cur.execute('UPDATE score SET time=' + str(score.time) + ', status_id=' + str(score.status) + ' WHERE id = '+ str(score.id))
        con.commit()  
        con.close()
    except Exception as e:
        print(str(e))




