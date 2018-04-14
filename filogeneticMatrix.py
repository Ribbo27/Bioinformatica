#!/usr/bin/python
# coding=utf-8

import sys 
import re
import random



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
    nodeList = map(lambda x: x[0], edgeList)
    nodeList = map(lambda x: x[1], edgeList)
    charList = map(lambda x: x[2], edgeList)
    randEdgeList = list()

    nodeList = list(set(nodeList))
    for i in range(len(match)):
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



with open(sys.argv[1],'r') as input_file:
    file = input_file.read()
# edgeList = Lista di tuple (node1, node2, carattere)
edgeList = re.findall('^(\d+)\s+(\d+)\s+\{\'weight\'\:\s+([-]*\d+)\}$',file,re.M)

if len(sys.argv) == 2:
    #STAMPA MATRICE FILOGENETICA
    print("Caso 1")
elif len(sys.argv) == 3:
    if sys.argv[2].lower() == "--shuffle":
        edgeList = shuffle(edgeList)
elif len(sys.argv) == 4:
    if sys.argv[2].lower() == "--rows" and is_number(sys.argv[3]) and int(sys.argv[3]) <= len(edgeList):
        n = int(sys.argv[3])
        print(n)
        #TO DO
    else:
        print("Error: Invalid argument!")
        sys.exit()            
elif len(sys.argv) == 5:
    if sys.argv[2].lower() == "--shuffle" and sys.argv[3].lower() == "--rows" and is_number(sys.argv[4]) and int(sys.argv[4]) <= len(edgeList):
        edgeList = shuffle(edgeList)
        n = int(sys.argv[4])
        print(n)
        #TO DO
    if sys.argv[2].lower() == "--rows" and is_number(sys.argv[3]) and int(sys.argv[3]) <= len(edgeList) and sys.argv[4].lower() == "--shuffle":
        n = int(sys.argv[3])
        edgeList = shuffle(edgeList)
        print(n)
        #TO DO
    else:
        print("Error: Invalid argument!")
        sys.exit()    
else:
    print("Error: Invalid argument!")
    sys.exit()

