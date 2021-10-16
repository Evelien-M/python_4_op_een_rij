import random

from opponent.opponent import Opponent

class ImpossibleOpponent(Opponent):
    def __init__(self):
        pass

    def DoMove(self,table):
        moves = []
        for i in range(table.w):
            moves.append(i)
        random.shuffle(moves)
        count = 0
        for x in range(len(moves)):
            if table.CanAdd(moves[x],2):
                count = count + 1
            if count == 2:
                break

        