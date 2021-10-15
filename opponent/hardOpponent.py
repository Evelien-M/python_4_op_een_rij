from opponent.opponent import Opponent

class HardOpponent(Opponent):
    def __init__(self):
        pass

    def DoMove(self,table):
        moves = [0,1,2,3,4,5,6]
        for x in range(len(moves)):
            if table.CanAdd(moves[x],2):
                break
