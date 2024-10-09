# Crea, modifica e imprime diccionarios con nombres de paises

import os; os.system("cls")

paises = {      "Argentina" : 100,
                "Brasil"    : 200,
                "Colombia"  : 300,
                "Chile"     : 400,
                "Ecuador"   : 500,
                "Bolivia"   : 600,
                "Jamaica"   : 700,}

print("Diccionario ", paises, len(paises))

paises["Brasil"] = 250
paises["Chile"] = 450

paises.update({"Bolivia":650})
paises.update({"Jamaica":750})

print("\nDiccionario Modificado ", paises, len(paises))
