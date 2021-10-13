class Table:
    def __init__(self):
        self.w = 7
        self.h = 6
        self.Table = [[0 for x in range(self.w)] for y in range(self.h)] 

    # parameter value toevoegen er is een bug dat value altijd 0 is
    def CanAdd(self,x,input):
        for y in range(self.h):
            value = self.Table[y][x]
            if value == 0:
                if y == self.h - 1:
                    self.Table[y][x] = input 
                    print(value)
                    return True
                else: 
                    if self.Table[y + 1][x] != 0:
                        self.Table[y][x] = input
                        return True 
        return False

    def IsCompleted(self):
        pass

        


