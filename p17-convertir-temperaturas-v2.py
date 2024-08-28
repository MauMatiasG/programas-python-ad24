# Convertir temperaturas de celcius a farenheit y viceversa

import os; os.system("cls")

print("Convertir temperaturas de celcius a farenheit y viceversa\n")

print("[ 1 ] Convertir de Farenheit a Celcius")
print("[ 2 ] Convertir de Celcius a Farenheit")
print("[ 3 ] Salir")

op = int(input("Elige ? "))

if op == 1:
    print("Convertiendo de Farenheit a Celcius")
    temp = float(input("Dame los grados Farenheit ? "))
    res = (temp - 32 ) * 5 / 9
    print(f"{temp} Farenheit equivale a {res} Celcius")
elif op == 2:
    print("Convertiendo de Celcius a Farenheit")
    temp = float(input("Dame los grados Celcius ? "))
    res = (temp * 9 / 5 ) + 32
    print(f"{temp} Celcius equivale a {res} Farenheit")    
elif op == 3:
    print("\nTe vas por que tu quieres ... gracias")
else: 
    print("\nOpcion erronea ...")

print("\n Proceso terminado ...")
