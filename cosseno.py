from math import *

x1 = pi/6
x2 = pi/3
n = 0
i = 2
cosseno1 = cosseno2 = seno = 0
for c in range(n,i+1):
    cosseno1 += (((-1)**c)*x1**(2*c))/factorial(2*c) #0.8660538834157472

    cosseno2 += (((-1)**c)*x2**(2*c))/factorial(2*c) #0.501796201500181

cos(pi/6) #0.8660254037844387

cos(pi/3) #0.5000000000000001

print(f'O cos(pi/6) é {cosseno1}')
print(' ')
print(f'O cos(pi/3) é {cosseno2}')
print(' ')
print('Comparando com a biblioteca "math"')
print(cos(pi/6))
print(cos(pi/3))

x3 = 1.2*pi/180
for c in range(n, i+1):
    seno += (((-1)**c)*x3**(2*c+1))/factorial(2*c+1)
print(seno)