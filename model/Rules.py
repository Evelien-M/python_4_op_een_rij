class Rules:
    def Check(self,table,score,value):
        self.table = table
        self.score = score
        self.value = value
        if self.CheckHorizontal():
            if self.CheckVertical():
                if self.CheckDiagonalNWZO():
                    if self.CheckDiagonalNOZW():
                        return True

        print("won")
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
        return True

    def CheckDiagonalNWZO(self):
        return True

    def CheckDiagonalNOZW(self):
        return True

