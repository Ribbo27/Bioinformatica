#!/usr/bin/python
# coding=utf-8

import sys 
import re
import random

def findNodeRoot(edgeList):  #Return root nodes
	for root in edgeList:
		rootCounter=0
		for elem in edgeList:
			if (int(root[0])==int(elem[1])):
				rootCounter=rootCounter+1
		if (rootCounter==0):
			return root[0]
	return 0 

def findLeaves(edgeList):    #Return list of leaves
	listLeaves=list()
	for leaves in edgeList:
		leavesCounter=0
		for elem in edgeList:
			if(int(leaves[1])==int(elem[0])):
				leavesCounter=leavesCounter+1
		if (leavesCounter==0):
			listLeaves.append(leaves[1])
	listLeaves = list(set(listLeaves))
	print(listLeaves)
	print(len(listLeaves))
	return listLeaves
							
def builder(nodeList, charList1):
    
    #charList[:] = [char for char in charList if char >= 0]   # List of all positive characters

    nodes = len(nodeList)                                   # Number of nodes
    characters = len(charList1)                          # Number of character

    # Matrix building
    Matrix = [[0 for x in range(characters)] for y in range(nodes)]
    return Matrix

def returnPos(node,list):#return 
	#try:
	flag=False
	k=0
	while(flag==False):
		if(int(node)==int(list[k])):
			flag=True
		else:
			k=k+1
	return k
	#TROVA SEMPRE UN K 
	#CODICE MORTO 
	#except:
	#	print("Errore")
	

def arrayChar(edgeList,node):
	if(int(node)==int(0)): #TO DO: Function findNodeRoot
		return listChar
	else:
		for i in range(len(edgeList)):
			if (int(node)==int(edgeList[i][1])):
				#print(edgeList[i][1])
				listChar.append(edgeList[i][2])
				#print(listChar)
				arrayChar(edgeList,edgeList[i][0])
	#print(listChar)
	return listChar

def shuffle(matrix):
	newM=[]
	for i in range(len(matrix[0])):
		col = []
		for j in range(len(matrix)):
			col.append(matrix[j][i])
		newM.append(col)
	#print("newM:\n",newM,"\n")
	prova = len(newM)
	matrixF=[]
	while(prova>0):
		u=random.randint(0, (len(newM)-1))
		matrixF.append(newM.pop(u))
		prova=prova-1
	#print("matrixf:\n",matrixF)
	#print(len(matrixF))
	matrixFF = []
	for i in range(len(matrixF[0])):
		row = []
		for j in range(len(matrixF)):
			row.append(matrixF[j][i])
		matrixFF.append(row)
	#print("matrixFF:\n",matrixFF,"\n\n")
	prova=len(matrixFF)
	final=[]
	while(prova>0):
		u=random.randint(0, (len(matrixFF)-1))
		final.append(matrixFF.pop(u))
		prova=prova-1
	print("final:\n",final)



	

def matrixGen(edgeList, nodeList, matrix):  
	nodeList.sort()
	for row in nodeList:
		del listChar[0:len(listChar)]  #Svuoto lista 
		lineMatrix=arrayChar(edgeList, row)
		#print(lineMatrix)
		listCharLose=list() #Lista di caratteri da eliminare 
		lineMatrix1=list()  #List of characters without lose char 
		for char in lineMatrix:
			if(int(char)>=0):
				if (int(char) not in listCharLose):
					lineMatrix1.append(char)
			else:
				listCharLose.append((int(char)*-1))
		#print(lineMatrix1)
		charList1.sort()
		for col in lineMatrix1:
			matrix[returnPos(row,nodeList)][returnPos(col,charList1)]=1
	lineMatrix=list()
	#print(matrix)
    #print route
	return matrix


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
listChar=list()		#List of all characters for nodes 
with open(sys.argv[1],'r') as input_file:   # Opening input file
    file = input_file.read()                # Reading whole file

edgeList = re.findall('^(\d+)\s+(\d+)\s+\{\'weight\'\:\s+([-]*\d+)\}$',file,re.M)

#edgeList[:] = [x for x in edgeList if int(x[2]) >= 0]    
nodeList = list(map(lambda x: int(x[0]), edgeList))         # List of all nodes construction
nodeList.extend(map(lambda x: int(x[1]), edgeList))
nodeList = list(set(nodeList))
charList = list(map(lambda x: int(x[2]), edgeList))          # List of all characters
charList1=[item for item in charList if item>=0]		#List of all positive characters
charList.sort()
matrix = builder(nodeList, charList1)


#listaTest = [(1, 5, 9), (4, 6, 0), (1, 7, 3), (3, 8, 0), (4, 3, 7), (3, 2, 6), (1, 4, 12)]
#nodeTest = [1, 5, 4, 6, 7, 3, 8, 2]
#matrixGen(edgeList, nodeList, matrix)

if len(sys.argv) == 2:
	print("caso 1")
	#print(charList1)
	matrix=matrixGen(edgeList, nodeList, matrix)
	with open("output.txt", "w") as f:
		for elem in matrix:
			f.write(" ".join((str(elem).strip('[]').split(","))))
			f.write("\n")

elif len(sys.argv) == 3:
    if sys.argv[2].lower() == "--shuffle":
        matrix=matrixGen(edgeList, nodeList, matrix)
        shuffle(matrix)
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
        #print(n)
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

