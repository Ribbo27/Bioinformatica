#!/usr/bin/python
# coding=utf-8

import sys 
import re
import random

def builder(nodeList, charList):
    
    #charList[:] = [char for char in charList if char >= 0]   # List of all positive characters

    nodes = max(nodeList)                                   # Number of nodes
    characters = len(charList)                              # Number of character

    # Matrix building
    Matrix = [[2 for x in range(characters)] for y in range(nodes)]
    return Matrix

def matrixGen(edgeList, nodeList, matrix):

    route = []
    node = 8
    #for j in range(len(nodeList)):
    #    node = nodeList[j]
    print edgeList
    for i in range(len(edgeList)):
        
        if edgeList[i][1] == node:
            route.append(edgeList[i])
            node = int(edgeList[i][0])
            print node
    
    #print route

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

#edgeList[:] = [x for x in edgeList if int(x[2]) >= 0]    

nodeList = (map(lambda x: int(x[0]), edgeList))         # List of all nodes construction
nodeList.extend(map(lambda x: int(x[1]), edgeList))
nodeList = list(set(nodeList))
charList = map(lambda x: int(x[2]), edgeList)           # List of all characters

charList.sort()

matrix = builder(nodeList, charList)

#listaTest = [(1, 5, 9), (4, 6, 0), (1, 7, 3), (3, 8, 0), (4, 3, 7), (3, 2, 6), (1, 4, 12)]
#nodeTest = [1, 5, 4, 6, 7, 3, 8, 2]

matrixGen(edgeList, nodeList, matrix)

if len(sys.argv) == 2:
    matrix = matrixGen(edgeList, nodeList, matrix)
    print("Caso 1")
elif len(sys.argv) == 3:
    if sys.argv[2].lower() == "--shuffle":
        print('prova')
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
        n = int(sys.argv[4])
        print(n)
        #TO DO ********************
    if sys.argv[2].lower() == "--rows" and is_number(sys.argv[3]) and int(sys.argv[3]) <= len(edgeList) and sys.argv[4].lower() == "--shuffle":
        n = int(sys.argv[3])
        print(n)
        #TO DO ********************
    else:
        print("Error: Invalid argument!")
        sys.exit()    
else:
    print("Error: Invalid argument!")
    sys.exit()

