print('------SECUENCIA DE ARMONICOS------\n')

n=int(input('HASTA CUAL ARMÓNICO: '))

suma = 0.0

for i in range(1,n+1):
    if i ==1:
        print(f'1', end=' ')
    else:
        print(f'+ 1/{i}', end=' ')
    suma = suma + (1/i)

print('\n\nSUMA = ', suma)