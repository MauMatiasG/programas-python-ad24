# Segunda ley de newton (fuerza = masa * aceleracion)

import os; os.system("cls")

print("Calculando valores de la segunda ley de newton\n")
print("[ 1 ] Caclualr la fuerza")
print("[ 2 ] Caclualr la masa")
print("[ 3 ] Caclualr la aceleracion")

op = int(input("Elige una ocpion ? "))

if op == 1:
    print("\n Calculando la fuerza ...")
    m = int(input("Dame la masa ? "))
    a = int(input("Dame la aceleracion ? "))
    f = m * a
    print(f"La fuerza es {f}")
elif op == 2:
    print("\n Calculando la masa ...")
    f = int(input("Dame la fuerza ? "))
    a = int(input("Dame la aceleracion ? "))
    m =  f / a
    print(f"La masa es {m}")
elif op == 3:
    print("\n Calculando la aceleracion ...")
    f = int(input("Dame la fuerza ? "))
    m = int(input("Dame la masa ? "))
    a =  f / m
    print(f"La aceleracion es {a}")
else:
    print("\nOpcion invalida !!")