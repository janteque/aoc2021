import numpy as np
import re

regexLine = '(\d*),(\d*) -> (\d*),(\d*)'

class line:

    x0 = 0
    y0 = 0
    xf = 0
    yf = 0
    isValid = False
    def __init__(self, linedef):
        self.points = []
        match = re.search(regexLine, linedef)
        self.x0 = int(match.group(1))
        self.y0 = int(match.group(2))
        self.xf = int(match.group(3))
        self.yf = int(match.group(4))
        self.points.append([int(match.group(1)), int(match.group(2))]) #add first point
        self.points.append([int(match.group(3)), int(match.group(4))]) #add last point
        self.addpoints()

    def addpoints(self):
        if len(self.points) == 2:
            if self.points[0][0] == self.points[1][0]:
                #calculate
                #print("calculate horizontal line %s" % self.points)
                self.isValid = True
                for n in range(min(self.points[0][1], self.points[1][1])+1, max(self.points[0][1],self.points[1][1])):
                    self.points.append([self.points[0][0], n])
                    #print("added point %s " % [self.points[0][0], n])
            elif  self.points[0][1] == self.points[1][1]:
                #print("calculate vertical line %s" % self.points)
                self.isValid = True
                for n in range(min(self.points[0][0], self.points[1][0])+1, max(self.points[0][0],self.points[1][0])):
                    self.points.append([n,self.points[0][1]])
                    #print("added point %s " % [n,self.points[0][1]])
            else:
                print("line %s not valid" % self.points)
        
lines = []

minx = 0
miny = 0
maxx = 0
maxy = 0

with  open("input_5.txt", "r") as f:
    l = f.readline()
    while l:
        templine = line(l)
        minx = min(minx, templine.x0, templine.xf)
        maxx = max(maxx, templine.x0, templine.xf)
        miny = min(miny, templine.y0, templine.yf)
        maxy = max(maxy, templine.y0, templine.yf)
        lines.append(templine)
        l = f.readline()

diagram = np.zeros((maxx+1, maxy+1),dtype=int)

for l in lines:
    if l.isValid:
        for p in l.points:
            #print(p)
            diagram[p[1], p[0]] += 1

points = diagram[ np.where(diagram > 1) ]

print (diagram)
print ("Total points > 1: %s" % len(points))
