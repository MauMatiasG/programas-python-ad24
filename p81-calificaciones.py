# Materias y calificiaciones en un diccionario

import os; os.system("cls")

materias = ["Fisica", "Quimica", "Matematicas", "Geografia", "Estadistica"]
califs = [10, 9, 8, 7.5, 6]


print("Listas originales : ", materias, califs)

# Unir listas en un diccionario
notas = dict(zip(materias, califs))
print("Todo :", notas , len(notas))
# Agregar
notas.update({"Ingles":10})
notas.update({"Programacion":7})
print("Todo :", notas , len(notas))
#Actualizar
notas.update({"Fisica":9, "Quimica":10})
print("Todo :", notas , len(notas))
#Remover
notas.pop("Fisica")
notas.popitem()
print("Todo :", notas , len(notas))
#Actualizar
notas["Geografia"] = 8
notas["Estadistica"] = 7
print("Todo :", notas , len(notas))
#Iterar
s = 0
print("\Materias y calificaciones")
for m, c in notas.items():
    print(f"{m:15} - {c:5}")
    s = s + c
print(f"\nSuma: {s} - Promedio {s/len(notas)}")

#Borrar
notas.clear()
print(notas, len(notas))