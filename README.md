# Bioinformatica

Progetto Elementi di Bioinformatica aprile 2018

Scrivere un programma che riceve in input un albero descritto come 
una lista di archi (allego un esempio).

Ogni riga corrisponde ad un arco. Ad esempio, la riga 

    3 82 {'weight': 7}

indica che esiste un arco che collega il nodo numero 3 con il nodo numero 82 
e tale arco è etichettato 7+ (corrisponde all'acquisizione del carattere 7).

Se il peso è negativo 
    
    1 6 {'weight': -12}

il carattere in questione viene perso e l'arco viene etichettato "12-".

Le opzioni a riga di comando, entrambe opzionali, devono essere:

    --shuffle 
        se presente bisogna permutare casualemente i numeri di nodi e di carattere
    --rows N 
        in caso bisogna considerare solo N nodi che però devono includere tutte le foglie dell'albero


Inoltre, il programma deve calcolare la matrice binaria associata all'albero, 
dove ogni casella M[i,j] della matrice M vale:

    1       Sse il percorso dell'albero dal nodo i fino alla radice, 
            contiene l'arco etichettato j+ ma non contiene l'arco etichettato j-.


