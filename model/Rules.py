class Rules:
    # returns true is game is stil playable
    def Check(self,table,score,value):
        self.table = table
        self.score = score
        self.value = value
        if self.CheckHorizontal():
            if self.CheckVertical():
                if self.CheckDiagonalNWZO():
                    if self.CheckDiagonalNOZW():
                        return True

        return False


    def CheckHorizontal(self):
        for y in range(self.table.h):
            amount = 0
            for x in range(self.table.w): 
                if self.table.Table[y][x] == self.value:
                    amount = amount + 1
                else:
                    amount = 0
                if amount == 4:
                    return False 
        return True

    def CheckVertical(self):
        for x in range(self.table.w):
            amount = 0
            for y in range(self.table.h): 
                if self.table.Table[y][x] == self.value:
                    amount = amount + 1
                else:
                    amount = 0
                if amount == 4:
                    return False 
        return True

    def CheckDiagonalNWZO(self):
        for y in range(self.table.h - 3):
            for x in range(self.table.w - 3):
                if self.table.Table[y][x] == self.value:
                    if self.table.Table[y+1][x+1] == self.value:
                        if self.table.Table[y+2][x+2] == self.value:
                            if self.table.Table[y+3][x+3] == self.value:
                                return False
        return True

    def CheckDiagonalNOZW(self):
        return True
        for y in range(self.table.h - 3):
            for x in range(3,self.table.w):
                if self.table.Table[y][x] == self.value:
                    if self.table.Table[y+1][x-1] == self.value:
                        if self.table.Table[y+2][x-2] == self.value:
                            if self.table.Table[y+3][x-3] == self.value:
                                return False
        return True

