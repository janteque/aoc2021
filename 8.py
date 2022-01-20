import numpy as np
import pandas as pd



signal_patterns = []
output_values = []


def check_if_equal(list_1, list_2):
    """ Check if both the lists are of same length and if yes then compare
    sorted versions of both the list to check if both of them are equal
    i.e. contain similar elements with same frequency. """
    if len(list_1) != len(list_2):
        return False
    return sorted(list_1) == sorted(list_2)

def process_line(line):
    parts = line.rstrip().split("|")
    patterns = parts[0].strip().split(" ")
    output = parts[1].strip().split(" ")

    digits={}

    #detects the different digits based on these rules 
    # 1 == 2 lines
    # 4 == 4 lines
    # 7 == 3 lines
    # 8 == 7 lines
    # 9 == 6 lines, including 7 and 4
    # 6 == 6 lines, not including 1
    # 0 == 6 lines, not 9 not 6
    # 3 == 5 lines including 1
    # 5 == 5 lines, included in 6
    # 2 == 5 lines, not 3 not 5
    digits[1] = list(list(filter(lambda p: len(p) == 2, patterns))[0])
    digits[4] = list(list(filter(lambda p: len(p) == 4, patterns))[0])
    digits[7] = list(list(filter(lambda p: len(p) == 3, patterns))[0])
    digits[8] = list(list(filter(lambda p: len(p) == 7, patterns))[0])
    digits[9] = list(list(filter(lambda p: (len(p) == 6 and all(elem in list(p) for elem in digits[7]) and all(elem in list(p) for elem in digits[4])) , patterns))[0])
    digits[6] = list(list(filter(lambda p: (len(p) == 6 and not(all(elem in list(p) for elem in digits[1]))) , patterns))[0])
    digits[0] = list(list(filter(lambda p: (len(p) == 6 and not(all(elem in list(p) for elem in digits[6]) or all(elem in list(p) for elem in digits[9]))) , patterns))[0])
    digits[3] = list(list(filter(lambda p: (len(p) == 5 and all(elem in list(p) for elem in digits[1])) , patterns))[0])
    digits[5] = list(list(filter(lambda p: (len(p) == 5 and all(elem in digits[6] for elem in list(p))) , patterns))[0])
    digits[2] = list(list(filter(lambda p: (len(p) == 5 and not(all(elem in list(p) for elem in digits[5]) or all(elem in list(p) for elem in digits[3]))) , patterns))[0])
   

    patterns_dict = {}
    number = 0
    for digit, patternlist in digits.items():
        patterns_dict["".join(patternlist)] = digit
        if(check_if_equal(patternlist, output[0])):
            number = number + 1000*digit
        if(check_if_equal(patternlist, output[1])):
            number = number + 100*digit
        if(check_if_equal(patternlist, output[2])):
            number = number + 10*digit
        if(check_if_equal(patternlist, output[3])):
            number = number + digit


    return (patterns, output, number)

result = 0

with  open("input_8.txt", "r") as f:
    l = f.readline()
    while l:
        (patt, out, number) = process_line(l)
        print("Result 8B - line %s" % number)
        result = result + number
        signal_patterns.append(patt)
        output_values.append(out)
        l = f.readline()

cont = 0

all_output_values = [item for sublist in output_values for item in sublist]

for o in all_output_values:
    if len(o) in [2,3,4,7]:
        cont += 1



print("Result 8A %s" % cont)

print("Result 8B %s" % result)
