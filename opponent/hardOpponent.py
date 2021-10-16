import random
from model.Rules import Rules
from opponent.opponent import Opponent
from model.Table import Content, Table

class HardOpponent(Opponent):
    def __init__(self):
        pass

    def DoMove(self,table):
        moves = []
        for i in range(table.w):
            moves.append(i)

        random.shuffle(moves)
        a = self.CheckWinningMove(moves,table)
        if a is not None:
            table.CanAdd(a,2)
        else: 
            b = self.CheckPlayerWinningMove(moves,table)
            if b is not None:
                table.CanAdd(b,2)
            else:
                c = self.IsBestMove(moves,table)
                if c is not None:
                    table.CanAdd(c,2)
                else:
                    for x in range(len(moves)):
                        if table.CanAdd(moves[x],2):
                            break

    def MakeCopy(self,table):
        copyTable = Table(table.w,table.h)
        for y in range(table.h):
            for x in range(table.w):
                copyTable.Table[y][x] = Content(table.Table[y][x].value)
        return copyTable


    # returns none if no winning moves are available
    def CheckWinningMove(self,moves,table):
        rule = Rules()
        for x in range(len(moves)):
            temp = self.MakeCopy(table)
            if temp.CanAdd(moves[x],2):
                if not rule.Check(temp,2):
                    return moves[x]
        return None


    def CheckPlayerWinningMove(self,moves,table):
        rule = Rules()
        for x in range(len(moves)):
            temp = self.MakeCopy(table)
            if temp.CanAdd(moves[x],1):
                if not rule.Check(temp,1):
                    return moves[x]
        return None

    def IsBestMove(self,moves,table):
        for x in range(len(moves)):
            temp = self.MakeCopy(table)
            if temp.CanAdd(moves[x],2):
                if self.CheckPlayerWinningMove(moves,temp) is None:
                    return moves[x]

        return None
