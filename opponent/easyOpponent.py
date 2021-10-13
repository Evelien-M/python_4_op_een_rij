import random

class EasyOpponent:
    def __init__(self):
        pass

    def DoMove(self,table):
        print("aaaaaaaaaaaaa")
        moves = [0,1,2,3,4,5,6]
        random.shuffle(moves)
        for x in range(len(moves)):
            if table.CanAdd2(moves[x]):
                break

        