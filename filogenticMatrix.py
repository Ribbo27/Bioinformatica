#Lettura progetto 

#Import 

import sys 
import re
import random

with open(sys.argv[1],'r') as input_file:
    file = input_file.read()

pattern = '^(\d+)\s+(\d+)\s+\{\'weight\'\:\s+([-]*\d+)\}$'
match=re.findall(pattern1,file,re.M)
flag=True
print(match)
print(len(match))

#Funzione RANDOM vuole mischiare nodi con nodi e caratteri con caratteri 
funzione = input('Che funzione vuoi utilizzare: (Random o RowsN)')
funzione=funzione.lower()
if funzione=='random':
    print("Funzione Random: Verranno mischiati i nodi e verrà creato un nuovo albero")
    random.shuffle(match)#Sbagliato 
    print(match)
#Funzione ROWSN:considero solo N nodi (I nodi sono massimo 131)
elif funzione=='rowns':
    print("Funzione RowsN: Verranno considerati i primi N nodi")
    nodes= int(input("Inserisci il numero di nodi che vuoi considerare: "))
    while flag:
        if nodes>=len(match):
            print("Il numero supera il numero massimo di nodi.")
            nodes=input("Inserisci un nuove numero:")
        else:
            flag=False
