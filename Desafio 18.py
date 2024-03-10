import math
z = float(input('Insira um ângulo: '))
x = math.sin(math.radians(z))
c = math.cos(math.radians(z))
v = math.tan(math.radians(z))
print (f'O seno desse ângulo é {x:.2f}, o cosseno é {c:.2f} e a tangente é {v:.2f}.')
