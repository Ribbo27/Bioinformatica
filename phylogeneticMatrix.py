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
			listLeaves.append(int(leaves[1]))
	listLeaves = list(set(listLeaves))
	return listLeaves

def rown (nodeList,root,listLeaves,number):
	listNodeN=list(listLeaves)	
	if(number>=len(listLeaves)):
		number=(number-len(listLeaves))
		while(number>0):
			node=random.choice(nodeList)
			if ((node!=root) and (node not in listLeaves) and (node not in listNodeN)):
				listNodeN.append(node)
				number=number-1
		return listNodeN
	else:
		sys.exit("Error: Invalid argument")

def shuffle(matrix):
	newM=[]
	for i in range(len(matrix[0])):
		col = []
		for j in range(len(matrix)):
			col.append(matrix[j][i])
		newM.append(col)
	index = len(newM)
	matrixF=[]
	while(index>0):
		u=random.randint(0, (len(newM)-1))
		matrixF.append(newM.pop(u))
		index=index-1
	matrixFF = []
	for i in range(len(matrixF[0])):
		row = []
		for j in range(len(matrixF)):
			row.append(matrixF[j][i])
		matrixFF.append(row)
	index=len(matrixFF)
	final=[]
	while(index>0):
		u=random.randint(0, (len(matrixFF)-1))
		final.append(matrixFF.pop(u))
		index=index-1
	return final

def returnPos(node,list):#return 
	flag=True
	k=0
	while(flag):
		if(int(node)==int(list[k])):
			flag=False
		else:
			k=k+1
	return k
	
def arrayChar(edgeList,node):
	if(int(node)==findNodeRoot(edgeList)): 
		return charForNode	
	else:
		for i in range(len(edgeList)):
			if (int(node)==int(edgeList[i][1])):
				charForNode.append(edgeList[i][2])
				arrayChar(edgeList,edgeList[i][0])
	return charForNode
		
def matrixGen(edgeList, nodeListN, matrix):  
	nodeListN.sort()
	matrix = [[0 for x in range(len(charListPositive))] for y in range(len(nodeListN))]
	for row in nodeListN:
		del charForNode[:]  #Svuoto lista 
		lineMatrix=arrayChar(edgeList, row)
		listCharLose=list() #Lista di caratteri da eliminare 
		lineMatrixFinal=list()  #List of characters without lose char 
		for char in lineMatrix:
			if(int(char)>=0):
				if (int(char) not in listCharLose):
					lineMatrixFinal.append(char)
			else:
				listCharLose.append((int(char)*-1))
		charListPositive.sort()	
		for col in lineMatrixFinal:
			matrix[returnPos(row,nodeListN)][returnPos(col,charListPositive)]=1
	LineMatrix=list()	
	print(matrix)
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

def stampa():
	with open("output.txt", "w") as f:
		f.write("Nodes: " + str(len(matrix)) + "   Characters: " + str(len(matrix[1])))
		f.write("\n\n")
		for elem in matrix:
			f.write(" ".join((str(elem).strip('[]').split(","))))
			f.write("\n")

# Globals variables
nodeList = []       # List to store all nodes
charList = list()   # List to store all characters
edgeList = []       # Tuple's list to store tree (node1, node2, character)
charForNode=list()		#List of all characters for nodes 
with open(sys.argv[1],'r') as input_file:   # Opening input file
    file = input_file.read()                # Reading whole file
	
edgeList = re.findall('^(\d+)\s+(\d+)\s+\{\'weight\'\:\s+([-]*\d+)\}$',file,re.M) #Regolar Esxpression
nodeList = list(map(lambda x: int(x[0]), edgeList))         # List of all nodes construction
nodeList.extend(map(lambda x: int(x[1]), edgeList))
nodeList = list(set(nodeList))
charList = list(map(lambda x: int(x[2]), edgeList))          # List of all characters
charListPositive=[item for item in charList if item>=0]		#List of all positive characters
listNodeN = list()  #List for rows N 
matrix = list()  #List final matrix

if len(sys.argv) == 2:
	matrix=matrixGen(edgeList, nodeList, matrix)
	stampa()
elif len(sys.argv) == 3:
	if (sys.argv[2].lower() == "--shuffle"):
		matrix=matrixGen(edgeList, nodeList, matrix)
		matrix=shuffle(matrix)
		stampa()
	else:
		sys.exit("Error: Invalid argument!")
		 
elif len(sys.argv) == 4:
	if((sys.argv[2].lower() == "--rows") and (is_number(sys.argv[3])) and (int(sys.argv[3]) <= len(edgeList))):
		n = int(sys.argv[3])
		leaves=findLeaves(edgeList)
		root=findNodeRoot(edgeList)
		nodeListN=rown(nodeList,root,leaves,n) 
		matrix=matrixGen(edgeList, nodeListN, matrix)
		stampa()   
	else:
		sys.exit("Error: Invalid argument!")
           
elif len(sys.argv) == 5:
    if ((sys.argv[2].lower() == "--shuffle") and (sys.argv[3].lower() == "--rows") and (is_number(sys.argv[4])) and (int(sys.argv[4]) <= len(edgeList))):
        n=int(sys.argv[4])
        leaves=findLeaves(edgeList)
        root=findNodeRoot(edgeList)
        nodeListN=rown(nodeList, root, leaves, n)
        matrix=matrixGen(edgeList, nodeListN, matrix)
        matrix=shuffle(matrix)
        stampa()
    elif ((sys.argv[2].lower() == "--rows") and (is_number(sys.argv[3])) and (int(sys.argv[3]) <= len(edgeList)) and (sys.argv[4].lower() == "--shuffle")):
        n=int(sys.argv[3])
        leaves=findLeaves(edgeList)
        root=findNodeRoot(edgeList)
        nodeListN=rown(nodeList, root, leaves, n)
        matrix=matrixGen(edgeList, nodeListN, matrix)
        matrix=shuffle(matrix)
        stampa()
    else:
        sys.exit("Error: Invalid argument!")    
else:
    sys.exit("Error: Invalid argument!")


