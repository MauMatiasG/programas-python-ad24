# Crea e itera un diccionario a partir de 2 listas de trabjadores y sueldos

import os; os.system("cls")

Nombres = ["Juan", "Pedro", "Manuel", "Elias", "Maria", "Felipe", "Julia", "Roberto"]
Sueldos = [4550.22, 8456.88, 1235.12, 9998.00, 12345.50, 29456.55, 12234.00, 2000.00]


print("Listas originales")
print(Nombres)
print(Sueldos)

Trabajadores = dict(zip(Nombres, Sueldos))

print("\nDiccionario resultante ", Trabajadores, len(Trabajadores))

print("\nIterando...")
s = 0

print("\nUsando las llaves", Trabajadores.keys())
for k in Trabajadores.keys():
    print(k, end=" - ")
print()

print("\nUsando los valores", Trabajadores.values())
for v in Trabajadores.values():
    print(v, end=" - ")
print()

print("\nUsando la llave y el valor en base a la llave")
for k in Trabajadores.keys():
    print(f"{k:<7} : {Trabajadores[k]}")
print()

print("\nUsando el para llave/valor items()")
for k, v in Trabajadores.items():
    print(f"{k:<7} : {v}")
    s = s + v

print(f"\nSuma: {s:,} - Promedio {s/len(Trabajadores):,.3f}")


