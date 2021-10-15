from flask import Flask, request, render_template, url_for, redirect
import database
from model.Rules import Rules
from opponent.easyOpponent import EasyOpponent
from model.Score import Score
from model.Table import Table

app = Flask(__name__)
table = None

@app.route('/',methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        playername = request.form['name'].upper()
        if len(playername) > 45 or len(playername) < 1 or playername == "*":
            return redirect('/')

        diff = request.form['difficulty']
        if diff != "easy" and diff != "hard":
            return redirect('/')

        width = request.form['width']
        height = request.form['height']
        try:
            width = int(width)
            height = int(height)
            if width < 4 or width > 9 or height < 4 or height > 9:
                raise ValueError('Wrong number.')
        except Exception:
            width = 7
            height = 6

        id = database.createGame(playername,diff,width,height)
        return redirect(url_for('game', id=id))
    else:
        scores = database.getHighscoreHomepage()
        return render_template("home.html",scores=scores)
        

@app.route('/game/<int:id>',methods=['GET', 'POST'])
def game(id):
    score = database.getScore(id)
    table = database.getGame(score)
    opponent = EasyOpponent()
    rule = Rules()

    if request.method == 'POST':
        column = request.form['column']
        c = int(column)

        if score.status == 1:
            if table.CanAdd(c,1):
                if not rule.Check(table,score,1):
                    score.status = 2
                if score.status == 1:
                    opponent.DoMove(table)
                    if not rule.Check(table,score,2):
                        score.status = 3

                if score.status == 1:
                    if table.IsCompleted():
                        score.status = 4
                        
                score.UpdateTime()
                database.updateScore(score)
                score = database.getScore(id)
                database.updateGame(id,table)

    return render_template("game.html",score=score,table=table)


@app.route('/scores/<string:table>/<string:order>/<int:page>/<string:name>',methods=['GET', 'POST'])
def scores(table,order,page,name):
    try:
        offset = int(page) * 20
    except Exception:
        offset = 0

    if (name == "*"):
        scores = database.getScoreAll(table,order,offset)
        total = database.getTotalAmountScoreAll()
    else:
        scores = database.getScoreName(name,table,order,offset)
        total = database.getTotalAmountScoreName(name)

    return render_template("scores.html",scores=scores,total=total,table=table,order=order,page=page)



if __name__ == '__main__':
    app.run(debug=True)

