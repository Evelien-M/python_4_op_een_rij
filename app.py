from flask import Flask, request, render_template, url_for, redirect
import database
import datetime
from opponent.easyOpponent import EasyOpponent
from model.Rules import Rules
from model.Score import Score
from model.Table import Table
import test


app = Flask(__name__)
table = None

@app.route('/',methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        playername = request.form['name'].upper()
        if len(playername) > 45 or len(playername) < 1:
            return redirect('/')

        diff = request.form['difficulty']
        if diff != "easy" and diff != "hard":
            return redirect('/')

        id = database.createGame(playername,diff)
        return redirect(url_for('game', id=id))
    else:
        scores = database.getHighscoreHomepage()
        return render_template("home.html",scores=scores)
        

@app.route('/game/<int:id>',methods=['GET', 'POST'])
def game(id):
    score = database.getScore(id)
    table = database.getGame(id)
    opponent = EasyOpponent()
    rule = Rules()

   # c = column - 1
    if request.method == 'POST':
        column = request.form['column']
        c = int(column)

        if table.CanAdd(c,1):
            rule.Check(table,score,1)
            if score.status == 1:
                opponent.DoMove(table)
            # rule.Check(table,score,2)
            database.updateGame(id,table)

    return render_template("game.html",score=score,table=table)




if __name__ == '__main__':
    app.run(debug=True)

