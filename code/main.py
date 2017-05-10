#!/usr/bin/python

import kociemba
from controls import *
from read_cube import *
import time
import subprocess


# Rotate side by 180 degrees to fit kociemba format (for yellow side only)
def rot180(seq):
    rotSeq = ''
    for i in range(len(seq)-1, -1, -1):
        rotSeq += seq[i]
    return rotSeq

# Permute side to fit kociemba format (for blue, orange, and white sides only) 
def permute(seq):
    perSeq = ''
    perSeq += seq[2]
    perSeq += seq[5]
    perSeq += seq[8]
    perSeq += seq[1]
    perSeq += seq[4]
    perSeq += seq[7]
    perSeq += seq[0]
    perSeq += seq[3]
    perSeq += seq[6]
    return perSeq

# Initialize the claws
initialize()

# Close claws
userInput = ''
while userInput != 'c':
    userInput = raw_input("Press c when ready to grip: ")
close()


############################
#     INSPECTION PHASE     #
############################


# Read input cube configuration from pixy cam

# (Inspect each side by rotating it)
# Camera is looking down on the cube (at the Yellow face)
# Front = Orange, Right = Blue, Left = Green, Up = Yellow, Down = White, Back = Pink

seq = ''

print('Inspecting yellow...')
openrl()

side = rot180(read())
side_ = side[0:4]
side_ += 'U'
side_ += side[5:]
seq += side_
print(side_)

rotate1()
print('Inspecting blue...')
side = permute(read())
side_ = side[0:4]
side_ += 'R'
side_ += side[5:]
seq += side_
print(side_)

rotate2()
print('Inspecting orange...')
side = permute(read())
side_ = side[0:4]
side_ += 'F'
side_ += side[5:]
seq += side_
print(side_)

rotate3()
print('Inspecting white...')
side = permute(read())
side_ = side[0:4]
side_ += 'D'
side_ += side[5:]
seq += side_
print(side_)

rotate2()
print('Inspecting green...')
side = read()
side_ = side[0:4]
side_ += 'L'
side_ += side[5:]
seq += side_
print(side_)

rotate3()
print('Inspecting pink...')
side = read()
side_ = side[0:4]
side_ += 'B'
side_ += side[5:]
seq += side_
print(side_)

# Return to original orientation
rotate4()
print('Done Inspecting!\n')

############################
#       SOLVING PHASE      #
############################

# Convert the cube configuration into kociemba format
#config = 'DRLUUBFBRBLURRLRUBLRDDFDLFUFUFFDBRDUBRUFLLFDDBFLUBLRBD'
print("Input Configuration: ")
#print(config)
print(seq)
print('\n')

# Pass the cube configuration into the kociemba solver
#solution = kociemba.solve(config)
solution = kociemba.solve(seq) 
print("Solution: ")
print(solution)
print('\n')

# Initialize the claws
initialize()

# Close claws
userInput = ''
while userInput != 'c':
    userInput = raw_input("Press c when ready to grip: ")
close()

# Solve the cube
print("Solving the cube...")
moves = solution.split()


'''
for m in moves:
    print(m)
    if m == 'F':
        turnF(0)
    elif m == "F'":
        turnF(1)
    elif m == "F2":
        turnF(2)
    elif m == 'R':
        turnR(0)
    elif m == "R'":
        turnR(1)
    elif m == "R2":
        turnR(2)
    elif m == 'L':
        turnL(0)
    elif m == "L'":
        turnL(1)
    elif m == "L2":
        turnL(2)
    elif m == 'B':
        turnB(0)
    elif m == "B'":
        turnB(1)
    elif m == "B2":
        turnB(2)
    elif m == 'U':
        turnU(0)
    elif m == "U'":
        turnU(1)
    elif m == "U2":
        turnU(2)
    elif m == 'D':
        turnD(0)
    elif m == "D'":
        turnD(1)
    elif m == "D2":
        turnD(2)
'''

