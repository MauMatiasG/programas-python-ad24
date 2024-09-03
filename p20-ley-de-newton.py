# Calcular la segunda ley de newton (f = m * a)

import os; os.system("cls")

print("Calcular la segunda ley de newton ( f = m * a )")
print("[ F ] fuerza  f = m * a ")
print("[ M ] Masa    m = f / a ")
print("[ A ] fuerza  a = f / m ")
op = input("Elige ? ").upper()

if op == "F":
    print("\n Calculando la fuerza ...")
    m = int(input("Dame la masa ? "))
    a = int(input("Dame la aceleracion ? "))
    f = m * a
    print(f"La fuerza es {f}")
elif op == "M":
    print("\n Calculando la masa ...")
    f = int(input("Dame la fuerza ? "))
    a = int(input("Dame la aceleracion ? "))
    m =  f / a
    print(f"La masa es {m}")
elif op == "A":
    print("\n Calculando la aceleracion ...")
    f = int(input("Dame la fuerza ? "))
    m = int(input("Dame la masa ? "))
    a =  f / m
    print(f"La aceleracion es {a}")
else:
    print("\nOpcion invalida ...")

print("\nProceso terminado ... ")