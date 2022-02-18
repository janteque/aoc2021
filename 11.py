from dis import dis
import sys
from colorama import Fore, Back, Style, init
from asciimatics.screen import Screen
from time import sleep
init()

resultA = 0

octopus = []

def flash(points_matrix, y, x):
    max_x = len(points_matrix[0])
    max_y = len(points_matrix)
    displ_x = [-1,0,1]
    displ_y = [-1,0,1]
    for d_x in displ_x:
        for d_y in displ_y:
            neighbour_x = x+d_x
            neighbour_y = y+d_y
            if  neighbour_x in range(0,max_x) and neighbour_y in range(0,max_y): #if displacement in range of the matrix +1 it
                n_value = points_matrix[neighbour_y][neighbour_x]
                if n_value in range(1,10):
                    points_matrix[neighbour_y][neighbour_x] +=1



def pretty_print_old(matrix):
    x = 0
    y = 0
    for line in matrix:
        for n in line:
            if n == 0:
                print(Fore.RED + str(n) + Style.RESET_ALL, end='')
            else:
                print(n, end='')
        print("\r")

def pretty_print(matrix, screen, step):
    y = 0
    for line in matrix:
        x = 0
        for n in line:
            if n == 0:
                screen.print_at(n, x, y, 1)
            else:
                screen.print_at(n, x, y)
            x += 1
        y += 1
        screen.print_at("STEP " + str(step), 0, len(matrix)+2, 1)


def process_step(matrix):
    for y, line in enumerate(matrix):
        for x, point in enumerate(line):
            matrix[y][x] +=1
    #flash
    flashes = 0
    while True:
        loop_flashes = 0
        for y, line in enumerate(matrix):
            for x, point in enumerate(line):
                if(point > 9):
                    matrix[y][x] = 0
                    flash(matrix, y, x)
                    loop_flashes += 1
        flashes += loop_flashes
        if loop_flashes == 0:
            break
    return flashes



with open("input_11.txt", "r") as f:
    l = f.readline()
    while l:
        octopus.append(list(map(int, list(l.strip()))))
        l = f.readline()

def all_flashes(matrix):
    for line in matrix:
        for n in line:
            if n != 0:
                return False
    return True

def demo(screen):
    result = 0
    step = 0
    while True:
        step += 1
        #print("----------------- STEP %s -------------" % n)
        flashes = process_step(octopus)
        if step <= 100:
            result += flashes
        pretty_print(octopus, screen, step)
        screen.refresh()
        sleep(0.1)
        if all_flashes(octopus):
            break
    print("RESULT 11A %s" % result)
    print("RESULT 11B %s" % step)

Screen.wrapper(demo)





