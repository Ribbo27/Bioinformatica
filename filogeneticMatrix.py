#!/usr/bin/python
# coding=utf-8

import sys 
import re
import random
from functools import reduce

def builder(edgelist, nodeList, charList):
    
    nodeList = (map(lambda x: int(x[0]), edgelist))         # List of all nodes construction
    nodeList.extend(map(lambda x: int(x[1]), edgeList))
    charList = map(lambda x: int(x[2]), edgeList)           # List of all characters
    charList[:] = [char for char in charList if char > 0]   # List of all positive characters

    nodes = max(nodeList)                                   # Number of nodes
    characters = len(charList)                              # Number of character

    # Matrix building
    Matrix = [[0 for x in range(characters)] for y in range(nodes)]
    return Matrix

def findRoot(edgeList):
    roots = map(lambda x: x[0], edgeList) # List of possible roots
    nodes = map(lambda x: x[1], edgeList) # List of internal nodes
    c = 0                                 # Counter variable
    for i in range(len(roots)):
        tmp = roots[i]                    # Possible root
        for j in nodes:
            c = nodes.count(tmp)        
            if c == 0:                    # Check for root
                return tmp 
    print("Error: root not found!")       # You should never get here
    sys.exit()

def shuffle(edgeList):
    ''' 
        Shuffle is a function that mixes every 
        tuple's element inside a list

        The tuple are such (node1, node2, char)
        where node1 and node2 represent two nodes
        of a filogenetic tree while char represents
        the genetic character

        Keyword argument:
        --edgelist: List of tuples

        Return the edgetreelist shuffled
    '''
    
    randEdgeList = list()

    nodeList = list(set(nodeList))
    for i in range(len(edgeList)):
        randEdgeList.append((random.choice(nodeList), random.choice(nodeList), random.choice(charList)))
    return randEdgeList

def is_number(s):
    '''
        Is_number is a function that verify that checks 
        whether the parameter passed is a number or not

        Keyword argument:
        --s: value to check

        Return True if s is a number, False otherwise
    '''
    try:
        int(s)
        return True
    except ValueError:
        return False


# Globals variables
nodeList = []       # List to store all nodes
charList = list()   # List to store all characters
edgeList = []       # Tuple's list to store tree (node1, node2, character)

with open(sys.argv[1],'r') as input_file:   # Opening input file
    file = input_file.read()                # Reading whole file

edgeList = re.findall('^(\d+)\s+(\d+)\s+\{\'weight\'\:\s+([-]*\d+)\}$',file,re.M)

edgeList[:] = [x for x in edgeList if int(x[2]) >= 0]    

filoMatrix = builder(edgeList, nodeList, charList)

#listaTest = [(1, 5, 9), (4, 6, 0), (1, 7, 3), (3, 8, 0), (4, 3, 7), (3, 2, 6), (1, 4, -12)]

root = findRoot(edgeList)
#print root

if len(sys.argv) == 2:
    #TO DO ********************
    print("Caso 1")
elif len(sys.argv) == 3:
    if sys.argv[2].lower() == "--shuffle":
        randEdgeList = shuffle(edgeList)
elif len(sys.argv) == 4:
    if sys.argv[2].lower() == "--rows" and is_number(sys.argv[3]) and int(sys.argv[3]) <= len(edgeList):
        n = int(sys.argv[3])
        print(n)
        #TO DO ********************
    else:
        print("Error: Invalid argument!")
        sys.exit()            
elif len(sys.argv) == 5:
    if sys.argv[2].lower() == "--shuffle" and sys.argv[3].lower() == "--rows" and is_number(sys.argv[4]) and int(sys.argv[4]) <= len(edgeList):
        randEdgeList = shuffle(edgeList)
        n = int(sys.argv[4])
        print(n)
        #TO DO ********************
    if sys.argv[2].lower() == "--rows" and is_number(sys.argv[3]) and int(sys.argv[3]) <= len(edgeList) and sys.argv[4].lower() == "--shuffle":
        n = int(sys.argv[3])
        randEdgeList = shuffle(edgeList)
        print(n)
        #TO DO ********************
    else:
        print("Error: Invalid argument!")
        sys.exit()    
else:
    print("Error: Invalid argument!")
    sys.exit()

