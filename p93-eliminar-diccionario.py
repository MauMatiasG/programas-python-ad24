# Crea, elimina e imprime diccionarios

import os; os.system("cls")

municipios = {      "Apozol":1863, "Calera":1868, "Fresnillo":1554, "Guadalupe":1821, "Jalpa":1824, "Jerez":1824, "Loreto":1931,
"Mazapil":1824, "Momax":1857}

print("Diccionario ", municipios, len(municipios))

A = municipios.pop("Apozol")
print("\nApozol borrado")
print(municipios, len(municipios))

F = municipios.pop("Fresnillo")
print("\nFresnillo borrado")
print(municipios, len(municipios))

M = municipios.popitem()
print("\nMomax borrado")
print(municipios, len(municipios))

municipios.clear()
print("\nDiccionario borrado")
print(municipios, len(municipios))







