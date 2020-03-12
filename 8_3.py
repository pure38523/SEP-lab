from turtle import *

class Disk():
    def __init__(self, name, x, y, height, width):
        self.name = name
        self.x = x
        self.y = y
        self.height = height
        self.width = width

    def showdisk(self):
        pu()
        goto(self.x, self.y)
        pd()
        fillcolor("red")
        begin_fill()
        fd(self.width / 2)
        lt(90)
        fd(self.height)
        lt(90)
        fd(self.width)
        lt(90)
        fd(self.height)
        lt(90)
        fd(self.width / 2)
        end_fill()

    def newpos(self, x, y):
        self.cleardisk()
        self.x = x
        self.y = y
        self.showdisk()

    def cleardisk(self):
        pu()
        goto(self.x, self.y)
        pd()
        pencolor("white")
        fillcolor("white")
        begin_fill()
        fd(self.width / 2)
        lt(90)
        fd(self.height)
        lt(90)
        fd(self.width)
        lt(90)
        fd(self.height)
        lt(90)
        fd(self.width / 2)
        end_fill()
        
class Hanoi(object):
    def __init__(self, n = 3, start ="A", workspace = "B", destination = "C"):
        self.startp = Pole(start, 0, 0)
        self.workspacep = Pole(workspace, 150, 0)
        self.destinationp = Pole(destination, 300, 0)
        self.startp.showpole()
        self.workspacep.showpole()
        self.destinationp.showpole()
        for i in range (n):
            self.startp.pushdisk(Disk("d" + str(i), 0, i * 150, 20, (n-i) * 30 ))

    def move_disk(self, start, destination):
        disk = start.popdisk()
        destination.pushdisk(disk)
    
    def move_tower(self, n, s, d, w):
        if n == 1:
            self.move_disk(s, d)
        else:
            self.move_tower(n-1, s, w, d)
            self.move_disk(s, d)
            self.move_tower(n-1, w, d, s)
        
    def solve(self):
        self.move_tower(3, self.startp, self.destinationp, self.workspacep)

h = Hanoi()
h.solve