import random

from opponent.opponent import Opponent

class EasyOpponent(Opponent):
    def __init__(self):
        pass

    def DoMove(self,table):
        moves = []
        for i in range(table.w):
            moves.append(i)
        random.shuffle(moves)
        for x in range(len(moves)):
            if table.CanAdd(moves[x],2):
                break

        