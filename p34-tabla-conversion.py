# Imprimir una tabla de conversion peso a dolar

import os

while(True):
    os.system("cls")

    tc = 19.87

    while(True): # Pide valores hasat que pi < pf
        pi = float(input("Valor en pesos inicial: "))
        pf = float(input("Valor en pesos final: "))
        if pi < pf: 
            break

    c = pi

    print("\nPeso\tDolar")
    print("-"*15)
    while c <= pf:
        print(f" {c}\t{c/tc:.2f}")
        c+=1
    print("-"*15)

    if input("Deseas continuar (S/N) ").upper().startswith("N"): break

print("\nProceso terminado")