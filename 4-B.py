
import numpy as np

class board:

    def __init__(self):
        self.lines = []
        self.matrix = np.empty((0,5),int)
        self.awarded = False



    def addline(self, line):
        line = list(map(int, line))
        self.lines.append(line)
        self.matrix = np.append(self.matrix, np.array([line]), axis=0)
    
    ### checks if number is on board and return True if is a check
    def checkNumber(self, number):
        for line in self.lines:
            if number in line:
                line.remove(number)
                self.matrix = np.where(self.matrix == number, -1, self.matrix)
                self.calculateIsWinner()
                return True
        return False

    def calculateIsWinner(self):
        sumrows = np.sum(self.matrix,axis=1)
        sumcols = np.sum(self.matrix,axis=0)
        if -5 in sumcols or -5 in sumrows:
            self.awarded = True

    def getSumUnmarked(self):
        result = 0
        for line in self.lines:
            result += sum(line)
        return result




boards = []

with  open("input_4.txt", "r") as f:
    inputlines = f.readlines()
f.close()

numbers = inputlines.pop(0).split(",")


tempboard = board()
for inputline in inputlines:
    linenumbers = inputline.split()
    if len(linenumbers) == 0:
        if len(tempboard.lines) > 0:
            boards.append(tempboard)
        tempboard = board()
    else:
        tempboard.addline(linenumbers)

boards.append(tempboard)

firstWinner = False
lastboard = board()
lastnumber = -1

for n in numbers:  
    for board in boards:
        if board.awarded: #if already awarded, pick next board
            continue
        board.checkNumber(int(n))
        if board.awarded:
            lastboard = board
            lastnumber = int(n)
            if not firstWinner:
                print("Board awarded %s" % board.lines)
                result = board.getSumUnmarked() * int(n)
                print("Result first winner A: %d" % result)
                firstWinner = True
            continue
        

print("Last board awarded %s" % lastboard.lines)
resultB = lastboard.getSumUnmarked() *  lastnumber
print("Result last winner B: %d" % resultB)