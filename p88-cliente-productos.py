# Calcular la cantidad de productos y subtotal por cliente, usando listas de diccionarios

import os; os.system("cls")

n = int(input("Cuantas compras ? "))

compras = []

for i in range(1, n+1):
    print(f"\n------- Compra {i} ------")
    compra = {
        "cliente" : input("Nombre: "),
        "producto" : input("Producto: "),
        "cantidad" : int(input("Cantidad: ")),
        "precio"   : float(input("Precio: "))
    }
    compras.append(compra)

print(compras)

#Calcular cantidad de productos y subtotal por cliente
clientes = {}
for compra in compras:
    cliente = compra["cliente"] # Creamos una entrada al diccionario por cada ciente
    if cliente not in clientes:
        clientes[cliente] = {"cantidad":0, "subtotal":0} #creamos un sub diccionario por cada cliente
    clientes[cliente]["cantidad"] += compra["cantidad"]
    clientes[cliente]["subtotal"] += compra["cantidad"] * compra["precio"]

    # Imprime clientes y subtotales (diccionario de diccionarios)
    print(clientes)

    print("Datos finale")
    for cliente, datos in clientes.items():
        print()
        print("Cliente ", cliente)
        print("Cantidad ", datos["cantidad"])
        print("Subtotal ", datos["subtotal"])
