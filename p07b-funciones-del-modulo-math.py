# Ejemplificar el uso de algunas funciones de la libreria math

import math as mt

w = 10.64
x = 10
y = 20
z = 35

print(f"Los numeros son : {w}, {x}, {y}, {z}")
print(f"Maximo comun divisor    : { mt.gcd(x,y,z) }")
print(f"Valor Maximo           : { max(x,y,z) }")
print(f"Valor Minimo           : { min(x,y,z) }")
print(f"Elevar a una potencia  : { mt.pow(x, y)} \n")

print(f"Redondear hacia arriba : { mt.ceil(w) }")
print(f"Redondear hacia abajo  : { mt.floor(w) }")
print(f"Redondear              : { round(w) }")
print(f"Truncar                : { mt.trunc(w) }")
      