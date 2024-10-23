# Suma una lista de numeros, usando una funcion

def suma_lista(lista):
    s = 0
    for n in lista:
        s += n
    return s

nums = [10, 20, 30, 40, 50, 30, 20, 40, 30, 40, 50, 70]

res = suma_lista(nums)

print(f"La suma de la lista es {res}")