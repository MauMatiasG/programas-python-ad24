# Calcula el promedio de una lista, luego me regresa los que son mayores al promedio

def promedio(nums):
    s = 0
    for n in nums:
        s += n
    return s / len(nums)

def mayoresprom(nums, prom):
    mp = []
    for n in nums:
        if n > prom:
            mp.append(n)
    return mp

def leerdatos():
    datos=[]
    while True:
        d = int(input("Numero ? "))
        if d == -1: break
        datos.append(d)
    return datos

#Programa pincipal

import os; os.system("cls")
# nums = [9,8,7.5,6,9.5,7,10,6,7]
nums = leerdatos
prom = promedio(nums)
print("Promedio ", prom)

mayprom = mayoresprom(nums, prom)
print(mayprom, len(mayprom)) 