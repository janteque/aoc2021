
#array storing the nomber of fishes on each cycle. Index is remaining days
fishes = [0,0,0,0,0,0,0,0,0]



days =256

with  open("input_6.txt", "r") as f:
    l = f.readline()
    temp = l.split(",")
    temp = list(map(int, temp))
    for f in temp:
        fishes[f] += 1


def cycle(_fishes):
    newfishes = [0,0,0,0,0,0,0,0,0]

    for idx, f in enumerate(_fishes):
        if idx == 0: #move fishes in 0 to 8
            newfishes[8] += _fishes[0]
            newfishes[6] += _fishes[0]
        else:
            newfishes[idx-1] +=_fishes[idx]
    
    return newfishes


for d in range(days):
    fishes = cycle(fishes)


print(fishes)
print(sum(fishes))
