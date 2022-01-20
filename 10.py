

height_matrix = []
points_matrix = [] #matrix of Point() objects

low_points = []

open_close = {
    "{":"}",
    "(":")",
    "[":"]",
    "<":">"
}

corrupt_scores = {
    "}":1197,
    ")":3,
    "]":57,
    ">":25137
}

completion_scores = {
    "}":3,
    ")":1,
    "]":2,
    ">":4
}

def findMiddle(input_list):
    middle = float(len(input_list))/2
    if middle % 2 != 0:
        return input_list[int(middle - .5)]
    else:
        return (input_list[int(middle)], input_list[int(middle-1)])

resultA = 0
resultB = 0

def process_line(line):
    openchars = []
    corrupt_score = 0
    completion_score = 0
    for letter in line:
        if letter in open_close.keys():
            openchars.append(letter)
        else:
            closechar = openchars.pop()
            if letter != open_close[closechar]:
                print("Expected %s but found %s instead" % (closechar, letter))
                corrupt_score = corrupt_score + corrupt_scores[letter]
                break
    
    if corrupt_score == 0 :
        #calculate completion score
        openchars.reverse()
        print("openchars: %s" % (openchars))
        for o in openchars:
            completion_char = open_close[o]
            completion_score = completion_score*5 + completion_scores[completion_char]
    print("result completion_score: %s" % (completion_score))
    return (corrupt_score, completion_score)

completion_results = []

with open("input_10.txt", "r") as f:
    l = f.readline()
    while l:
        (corrupt_score, completion_score) = process_line(l.strip())
        resultA += corrupt_score
        if(completion_score != 0):
            completion_results.append(completion_score)
        l = f.readline()


print("result 10A: %s" % (resultA))
completion_results.sort()
print("result 10B: %s" % (findMiddle(completion_results)))
