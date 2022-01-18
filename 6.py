

fishes = []

days = 80

with  open("input_6.txt", "r") as f:
    l = f.readline()
    fishes = l.split(",")
    fishes = list(map(int, fishes))


def cycle(_fishes):
    newfishes = []

    for idx, f in enumerate(_fishes):
        if f == 0:
            _fishes[idx] = 6
            newfishes.append(8)
        else:
            _fishes[idx] = f-1
    
    _fishes.extend(newfishes)
    return _fishes


for d in range(days):
    fishes = cycle(fishes)


#print(fishes)
print(len(fishes))
