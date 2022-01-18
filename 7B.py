import enum
import numpy as np
import pandas as pd
from tqdm import tqdm

crabs_pos = []

minx = 0
maxx = 0

with  open("input_7.txt", "r") as f:
    l = f.readline()
    crabs_pos = l.split(",")
    crabs_pos = list(map(int, crabs_pos))

minx = min(crabs_pos)
maxx = max(crabs_pos)

#list of x positions
xpos = list(range(minx, maxx+1))

print("Total crabs: %s" % len(crabs_pos))

#dataframe with the crabs as indexes and positions as columns
data = np.zeros((len(crabs_pos), maxx - minx +1),dtype=int)
df = pd.DataFrame(data,  columns=xpos)

#populate dataframe with distances of each crab to each location
for idx_c, c in enumerate(tqdm(crabs_pos)):
    for idx_p, p in enumerate(xpos):
        #set value as the series between position and destination (1+2+3+...+n) being b = abs(p - c)
        n = abs(p - c)
        df.iloc[idx_c, idx_p] = n*(n+1)/2
    #print("Crab %s at position %s processed" % (idx_c, c))


#print (df)
#calculate the sum of each column
distances = df.apply(np.sum, 0)

#print(distances)

print("Best position is %s, total fuel is %s" % (distances.idxmin(), distances.min()))

