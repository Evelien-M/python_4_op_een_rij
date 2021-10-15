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
        score = Score(r[0],r[1],r[2],r[3],r[4],r[5],r[6],r[7])
        list.append(score)
    
    con.close()
    return list


def getScoreAll(table,order,offset):
    list = []
    try:
        con = sqlite3.connect(db_path)
        cur = con.cursor()
        for r in cur.execute('SELECT * FROM score INNER JOIN game_status ON score.status_id=game_status.id ORDER BY '+str(table)+' '+str(order)+' LIMIT 20 OFFSET ' + str(offset)):
            score = Score(r[0],r[1],r[2],r[3],r[4],r[5],r[6],r[7],r[9])
            
            list.append(score)
        
        con.close()
    except Exception as e: 
        print(str(e))
    
    return list

def getScoreName(name,table,order,offset):
    list = []
    try:
        con = sqlite3.connect(db_path)
        cur = con.cursor()
        for r in cur.execute('SELECT * FROM score INNER JOIN game_status ON score.status_id=game_status.id WHERE player = "'+str(name)+'" ORDER BY '+str(table)+' '+str(order)+' LIMIT 20 OFFSET ' + str(offset)):
            score = Score(r[0],r[1],r[2],r[3],r[4],r[5],r[6],r[7],r[9])
            
            list.append(score)
        
        con.close()
    except Exception as e: 
        print(str(e))
    
    return list

def getTotalAmountScoreName(name):
    i = 0
    try:
        con = sqlite3.connect(db_path)
        cur = con.cursor()
        for r in cur.execute('SELECT count(*) FROM score WHERE player = "'+ str(name) + '"'):
            i = r[0]
        
        con.close()
    except Exception as e: 
        print(str(e))
    
    return i

def getTotalAmountScoreAll():
    i = 0
    try:
        con = sqlite3.connect(db_path)
        cur = con.cursor()
        for r in cur.execute('SELECT count(*) FROM score'):
            i = r[0]
        
        con.close()
    except Exception as e: 
        print(str(e))
    
    return i


def createGame(name,difficulty,width,height):
    try:
        con = sqlite3.connect(db_path)
        cur = con.cursor()
        cur.execute("INSERT INTO score VALUES (NULL, '"+ str(name) +"', 0, '"+ str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) +"', '"+ str(difficulty) +"', "+ str(width) +", "+ str(height) +", 1)")
        id = cur.lastrowid
        for x in range(width): 
            for y in range(height):
                cur.execute("INSERT INTO game_table VALUES (" + str(id) + ", "+ str(x) +", "+ str(y) +", 0,0)")

        # add random oponent turn 
        r = random.randrange(0, 2)
        if r == 1:
            column = random.randrange(0,width)
            cur.execute("INSERT INTO game_table VALUES (" + str(id) + ", "+ str(column) +", "+ str(height - 1) +", 2,0)")

        con.commit()
        con.close()
        return id
    except Exception as e: 
        print(str(e))
        return None


def getGame(score):
    try:
        con = sqlite3.connect(db_path)
        cur = con.cursor()
        list = Table(score.width,score.height)
        for r in cur.execute('SELECT * FROM game_table WHERE id = '+ str(score.id)):
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
            score = Score(id,r[1],r[2],r[3],r[4],r[5],r[6],r[7])
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
        for x in range(table.w): 
            for y in range(table.h):
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




