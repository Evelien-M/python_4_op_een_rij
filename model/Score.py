from datetime import datetime
import time

class Score:
    def __init__(self,id,name,time,date,difficulty,status,statusName = None):
        self.id = id
        self.name = name
        self.time = time
        self.date = date
        self.difficulty = difficulty
        self.status = status
        self.statusName = statusName

    def UpdateTime(self):
        s = datetime.fromisoformat(self.date)
        dt = datetime.now()
        a = time.mktime(dt.timetuple())
        b = time.mktime(s.timetuple())
        c = a - b
        if c < 0:
            c = 0

        if c > 999:
            c = 999

        self.time = c


