
import numpy as np

class board:

    def __init__(self):
        self.lines = []
        self.matrix = np.empty((0,5),int)



    def addline(self, line):
        line = list(map(int, line))
        self.lines.append(line)
        self.matrix = np.append(self.matrix, np.array([line]), axis=0)
    
    ### checks if number is on board and return True if the line is completed
    def checkNumber(self, number):
        for line in self.lines:
            if number in line:
                line.remove(number)
                self.matrix = np.where(self.matrix == number, -1, self.matrix)
                if self.isWinner():
                    return True
        return False

    def isWinner(self):
        sumrows = np.sum(self.matrix,axis=1)
        sumcols = np.sum(self.matrix,axis=0)
        if -5 in sumcols or -5 in sumrows:
            return True
        else:
            return False

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

stop = False

for n in numbers:  
    if stop:
        break
    for board in boards:
        awarded = board.checkNumber(int(n))
        if awarded:
            print("Board awarded %s" % board.lines)
            result = board.getSumUnmarked() * int(n)
            print("Result A: %d" % result)
            stop = True
            break
        
    
