class Table:
    def __init__(self,width,height):
        self.w = width
        self.h = height
        self.Table = [[0 for x in range(self.w)] for y in range(self.h)] 

    def CanAdd(self,x,input):
        for y in range(self.h):
            value = self.Table[y][x].value
            if value == 0:
                if y == self.h - 1:
                    self.Table[y][x] = Content(input) 
                    return True
                else: 
                    if self.Table[y + 1][x].value != 0:
                        self.Table[y][x] = Content(input)
                        return True 
        return False

    def IsCompleted(self):
        count = 0
        for x in range(self.w):
            if self.Table[0][x].value != 0:
                count = count + 1

        if count == self.w:
            return True

        return False


        
class Content:
    def __init__(self,value, marked = 0):
        self.value = value
        self.marked = marked

