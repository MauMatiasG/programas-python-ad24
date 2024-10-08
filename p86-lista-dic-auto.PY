# Listas de diccionarios / Autos

import os; os.system("cls")

autos = [
    {"marca":"Ford", "modelo":"Mustang", "año":1964},
    {"marca":"VW", "modelo":"Jetta", "año":2015},
]

autos.append({"marca":"Chevrolet", "modelo":"Captiva", "año":2024})

print("Todos ", autos, len(autos))

for auto in autos:
    print(auto)

print("\nDatos en forma de tabla")
for k in autos[0].keys(): # Se imprime el titulo de la tabla (las llaves del diccionario)
    print(f"{k:<15}", end="")
print()

for auto in autos: # Para cada auto en autos, imprime los valores de cada auto
    for v in auto.values():
        print(f"{v:<15}", end="")
    print()

print("\nDatos en froma de registros:")
for auto in autos:
    for k, v in auto.items():
        print(f"{k:<12} : {v}")
    print()