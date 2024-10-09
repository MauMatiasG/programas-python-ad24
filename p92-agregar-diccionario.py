# Crea, agrega elemntos e imprime diccionarios de ventas

import os; os.system("cls")

ventas = {      "Juan"  : 1550,
                "Jose"  : 2600,
                "Maria" : 2220,}

print("Diccionario ", ventas, len(ventas))

ventas["Rocio"] = 2500
ventas["Mateo"] = 1567

ventas.update({"Andrea":9567})
ventas.update({"Miguel":1234})

print("\nDiccionario con elementos agregados ", ventas, len(ventas))
