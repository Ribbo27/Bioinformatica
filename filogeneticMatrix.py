#!/usr/bin/python
# coding=utf-8

import sys 
import re
import random

def builder(nodeList, charList1):
    
    #charList[:] = [char for char in charList if char >= 0]   # List of all positive characters

    nodes = len(nodeList)                                   # Number of nodes
    characters = len(charList1)                              # Number of character

    # Matrix building
    Matrix = [[0 for x in range(characters)] for y in range(nodes)]
    return Matrix

def arrayChar(edgeList,node):
	#print("node")
	#print(node)
	if(int(node)==int(0)):
		return listChar
	else:
		for i in range(len(edgeList)):
			if (int(node)==int(edgeList[i][1])):
				#print(edgeList[i][1])
				if (int(edgeList[i][1])<int(0)):
					#print("Entro if")
					number=int(edgeList[i][1])*-1
					for j in range(len(listChar)):
						if(listChar[j]==number):
							del listChar[j]
				else:
					listChar.append(edgeList[i][2])
					#print(listChar)
					arrayChar(edgeList,edgeList[i][0])
	#print(listChar)
	return listChar
	
	
def matrixGen(edgeList, nodeList, matrix):
	listCharLose=list()
    #for j in range(len(nodeList)):
    #    node = nodeList[j]
	nodeList.sort()
	#print(nodeList)
#print (edgeList)
	for i in range(len(nodeList)):
		#print("Dentro for")
		del listChar[0:len(listChar)]
		#print(listChar)
		lineMatrix=arrayChar(edgeList, i)
		#print("lenmatrix")
		#print(len(lineMatrix))
		#print("Stampo lineMatrix")
		#print(lineMatrix)
		for y in range(len(lineMatrix)):
			#print("lunghezza")
			#print(len(lineMatrix))	
			#print(y)
			if(int(lineMatrix[y])<0):
				listCharLose.append(lineMatrix[y])
				number=int(lineMatrix[y])*(-1)
				#print("numero")
				#print(number)				
				for x in range(len(lineMatrix)):
					if (int(lineMatrix[x])==number):
						listCharLose.append(lineMatrix[x])
				#print(listCharLose)
				#print(lineMatrix)
		#print(lineMatrix)
		lineMatrix=set(lineMatrix)
		#print(lineMatrix)
		listCharLose=set(listCharLose)
		#print(listCharLose)
		lineMatrix.difference_update(listCharLose)
		#print(lineMatrix)
		listCharLose=list()
		lineMatrix=list(lineMatrix)
		print(lineMatrix)
		for z in range(len(lineMatrix)):
			for j in range(len(charList1)):
				for k in range(len(lineMatrix)):
					if(int(lineMatrix[k])==j):
						matrix[i][j]=1
				#print(matrix)
	lineMatrix=list()
	print(matrix)
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
listChar=list()
with open(sys.argv[1],'r') as input_file:   # Opening input file
    file = input_file.read()                # Reading whole file

edgeList = re.findall('^(\d+)\s+(\d+)\s+\{\'weight\'\:\s+([-]*\d+)\}$',file,re.M)

#edgeList[:] = [x for x in edgeList if int(x[2]) >= 0]    

nodeList = list(map(lambda x: int(x[0]), edgeList))         # List of all nodes construction
nodeList.extend(map(lambda x: int(x[1]), edgeList))
nodeList = list(set(nodeList))
charList = list(map(lambda x: int(x[2]), edgeList))          # List of all characters
charList1=[item for item in charList if item>=0]

charList.sort()

matrix = builder(nodeList, charList1)

#listaTest = [(1, 5, 9), (4, 6, 0), (1, 7, 3), (3, 8, 0), (4, 3, 7), (3, 2, 6), (1, 4, 12)]
#nodeTest = [1, 5, 4, 6, 7, 3, 8, 2]

#matrixGen(edgeList, nodeList, matrix)

if len(sys.argv) == 2:
	print("caso 1")
	#print(charList1)
	matrixGen(edgeList, nodeList, matrix)
	
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

