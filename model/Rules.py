class Rules:
    # returns true is game is stil playable
    def Check(self,table,value):
        self.table = table
        self.value = value
        if self.CheckHorizontal():
            if self.CheckVertical():
                if self.CheckAscendingDiagonal():
                    if self.CheckDescendingDiagonal():
                        return True

        return False


    def CheckHorizontal(self):
        for y in range(self.table.h):
            amount = 0
            for x in range(self.table.w): 
                if self.table.Table[y][x].value == self.value:
                    amount = amount + 1
                else:
                    amount = 0
                if amount == 4:
                    self.table.Table[y][x].marked = 1
                    self.table.Table[y][x-1].marked = 1
                    self.table.Table[y][x-2].marked = 1
                    self.table.Table[y][x-3].marked = 1
                    return False 
        return True

    def CheckVertical(self):
        for x in range(self.table.w):
            amount = 0
            for y in range(self.table.h): 
                if self.table.Table[y][x].value == self.value:
                    amount = amount + 1
                else:
                    amount = 0
                if amount == 4:
                    self.table.Table[y][x].marked = 1
                    self.table.Table[y-1][x].marked = 1
                    self.table.Table[y-2][x].marked = 1
                    self.table.Table[y-3][x].marked = 1
                    return False 
        return True


    def CheckAscendingDiagonal(self):
        for y in range(3,self.table.h):
            for x in range(self.table.w - 3):
                if self.table.Table[y][x].value == self.value:
                    if self.table.Table[y-1][x+1].value == self.value:
                        if self.table.Table[y-2][x+2].value == self.value:
                            if self.table.Table[y-3][x+3].value == self.value:
                                self.table.Table[y][x].marked = 1
                                self.table.Table[y-1][x+1].marked = 1
                                self.table.Table[y-2][x+2].marked = 1
                                self.table.Table[y-3][x+3].marked = 1
                                return False

        return True

    def CheckDescendingDiagonal(self):
        for y in range(3,self.table.h):
            for x in range(3,self.table.w):
                if self.table.Table[y][x].value == self.value:
                    if self.table.Table[y-1][x-1].value == self.value:
                        if self.table.Table[y-2][x-2].value == self.value:
                            if self.table.Table[y-3][x-3].value == self.value:
                                self.table.Table[y][x].marked = 1
                                self.table.Table[y-1][x-1].marked = 1
                                self.table.Table[y-2][x-2].marked = 1
                                self.table.Table[y-3][x-3].marked = 1
                                return False
        return True


