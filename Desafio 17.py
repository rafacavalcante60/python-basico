import math
z = float(input('Insira o valor do cateto oposto: '))
x = float(input('Insira o valor do cateto adjacente: '))
hip = math.hypot(z,x)
print (f'A hipotenusa é {hip}.')
