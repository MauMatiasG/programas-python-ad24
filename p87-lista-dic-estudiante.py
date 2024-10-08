# Estudiantes y sus datos en una lista de diccionarios

import os; os.system("cls")

grupo = [
    {"nombre":"Carlos", "edad":45, "carrera":"Sistemas", "promedio":9},
    {"nombre":"Rocio", "edad":35, "carrera":"Sistemas", "promedio":10},
]

print("Inicial ", grupo, len(grupo))

while True:
    datos = {}
    nombre = input("Nombre : ")
    if nombre !="":
        datos["nombre"] = nombre
        datos["edad"] = int(input("Edad: "))
        datos["carrera"] = input("Carrera: ")
        datos["promedio"] = float(input("Promeido: "))
        grupo.append(datos)
    else:
        break

print("Todos ", grupo, len(grupo))

print("\nDatos en forma de tabla")
for k in grupo[0].keys(): # Se imprime el titulo de la tabla (las llaves del diccionario)
    print(f"{k:<15}", end="")
print()

for gpo in grupo: # Para cada auto en autos, imprime los valores de cada auto
    for v in gpo.values():
        print(f"{v:<15}", end="")
    print()

s = se = p = pe = 0

print("\nDatos en froma de registros:")
for al in grupo:
    s = s + al["promedio"] # Voy sumando los promedios de cada alumno
    for k, v in al.items():
        print(f"{k:<12} : {v}")
    print()


p = s / len(grupo)
pe = se / len(grupo)

print("La suma ", s, se)
print("El promedio ", p, pe)