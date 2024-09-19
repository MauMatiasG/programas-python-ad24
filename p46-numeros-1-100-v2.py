# Imprime numeros del 1 a 100 usando for

import os; os.system("cls")

""" print ( list(range (1,10) ) )
print ( list(range (1,10,2) ) )
print ( list(range (1,10,3) ) )
print ( list(range (10,0,-1) ) ) """

n = int(input("Hasta dodne ? "))

for x in range (1,n+1):
    print (x, end=" ")