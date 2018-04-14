#!/usr/bin/python
# coding=utf-8

import sys 
import re
import random

def shuffle(match):
    nodeList = map(lambda x: x[0], match)
    nodeList = map(lambda x: x[1], match)
    charList = map(lambda x: x[2], match)
    edgeList = list()

    nodeList = list(set(nodeList))
    for i in range(len(match)):
        edgeList.append((random.choice(nodeList), random.choice(nodeList), random.choice(charList)))
    return edgeList

def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

with open(sys.argv[1],'r') as input_file:
    file = input_file.read()
#Match = Lista di tuple (node1, node2, carattere)
match = re.findall('^(\d+)\s+(\d+)\s+\{\'weight\'\:\s+([-]*\d+)\}$',file,re.M)

if len(sys.argv) == 2:
    #STAMPA MATRICE FILOGENETICA
    print("Caso 1")
elif len(sys.argv) == 3:
    if sys.argv[2].lower() == "--shuffle":
        match = shuffle(match)
elif len(sys.argv) == 4:
    if sys.argv[2].lower() == "--rows" and is_number(sys.argv[3]) and int(sys.argv[3]) <= len(match):
        n = int(sys.argv[3])
        print(n)
        #TO DO
    else:
        print("Error: Invalid argument!")
        sys.exit()            
elif len(sys.argv) == 5:
    if sys.argv[2].lower() == "--shuffle" and sys.argv[3].lower() == "--rows" and is_number(sys.argv[4]) and int(sys.argv[4]) <= len(match):
        match = shuffle(match)
        n = int(sys.argv[4])
        print(n)
        #TO DO
    if sys.argv[2].lower() == "--rows" and is_number(sys.argv[3]) and int(sys.argv[3]) <= len(match) and sys.argv[4].lower() == "--shuffle":
        n = int(sys.argv[3])
        match = shuffle(match)
        print(n)
        #TO DO
    else:
        print("Error: Invalid argument!")
        sys.exit()    
else:
    print("Error: Invalid argument!")
    sys.exit()

