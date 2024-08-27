# Efectua operaciones matematicas sobre dos numeros flotantes

#x = 10.25 
#y = 2.5 

x = float(input("Dame el primer valor ? "))
y = float(input("Dame el segundo valor ? "))

suma = x+y
resta = x-y
mult = x*y
divi = x/y
dive = x//y
pot = x**y
res = x%y



print(f"Suma: {suma}\nResta: {resta}\nMultiplicacion: {mult}\nDivision: {divi}")
print(f"Divi Ent: {dive}\nPotencia: {pot:.2f}\nResiduo: {res}")



