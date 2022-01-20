

height_matrix = []
points_matrix = [] #matrix of Point() objects

low_points = []

bassins = {}

class Point:
    def __init__(self, x, y, height):
        self.x = x
        self.y = y
        self.height = height
        self.is_low_point = False
        self.bassin_id = ""

def get_neighbours(points_matrix, y, x):
    max_x = len(points_matrix[0])-1
    max_y = len(points_matrix)-1
    neighbours = []
    if x > 0 :
        neighbours.append(points_matrix[y][x-1])
    if x < max_x :
        neighbours.append(points_matrix[y][x+1])
    if y > 0 :
        neighbours.append(points_matrix[y-1][x])
    if y < max_y :
        neighbours.append(points_matrix[y+1][x])
    return neighbours

def process_point(point):
    max_x = len(points_matrix[0])-1
    max_y = len(points_matrix)-1
    x = point.x
    y = point.y
    neighbours = []

    if x > 0 :
        neighbours.append(points_matrix[y][x-1])
    if x < max_x :
        neighbours.append(points_matrix[y][x+1])
    if y > 0 :
        neighbours.append(points_matrix[y-1][x])
    if y < max_y :
        neighbours.append(points_matrix[y+1][x])

    if point.bassin_id != "":
        for n in neighbours:
            if n.height != 9 and n.bassin_id == "":
                n.bassin_id = point.bassin_id
                if n.bassin_id not in bassins:
                    bassins[n.bassin_id] = []
                bassins[n.bassin_id].append(n.height)
                process_point(n)
    
    return point



with open("input_9.txt", "r") as f:
    l = f.readline()
    while l:
        line = map(int, list(l.strip()))
        height_matrix.append(line)
        l = f.readline()


for y, line in enumerate(height_matrix):
    points_matrix.append([])
    for x, height in enumerate(line):
        neighbours = []
        neighbours = get_neighbours(height_matrix,y, x)
        points_matrix[y].append(Point(x,y,height))
        #print ("point at %s, %s: %s with neighbours %s" % (x,y,point, neighbours))
        if  all(i > height for i in neighbours):
            #print ("point Added")
            low_points.append(height)
            bassin_id = str(x) +":"+ str(y)
            points_matrix[y][x].is_low_point = True
            points_matrix[y][x].bassin_id = bassin_id
            bassins[bassin_id] = []
            bassins[bassin_id].append(height)

for line in points_matrix:
    map(process_point, line)

print("low_points: %s" % (low_points))
print("bassins: %s" % (bassins))



result = sum(low_points) + len(low_points)
print("result 9A: %s" % (result))

bassins_ordered= list(bassins.values())
bassins_ordered.sort(key=len, reverse=True)
print("bassins: %s" % (bassins_ordered))
print("Result 9B: %s" % (len(bassins_ordered[0]) * len(bassins_ordered[1]) * len(bassins_ordered[2])))