'''
1) a) Função que calcula o seno a partir da série de taylor'''
def taylor_seno(x, n):
    from math import factorial
    seno = 0
    for c in range(0,n):
        seno += (((-1)**c)*x**(2*c+1))/factorial(2*c+1)
    return seno

'b) x = pi/6 para os valores n = 3, n = 5 e n = 7'
from math import pi
import numpy as np
import matplotlib.pyplot as plt
x1 = pi/6
print(taylor_seno(x1,3))
print(' ')
print(taylor_seno(x1,5))
print(' ')
print(taylor_seno(x1,7)) #dentre as tres é a melhor aproximação

'c) mesma coisa da b) mas p/ x = 3pi/4'
x2 = 3*pi/4
print(' ')
print('Para x = 3pi/4')
print(taylor_seno(x2,3))
print(' ')
print(taylor_seno(x2,5))
print(' ')
print(taylor_seno(x2,7))

xg = np.array([x1, x2])
y = np.array([3,5,7,9])
plt.xlabel(xg)
plt.ylabel(taylor_seno(xg,y))
plt.title('Série de Taylor')
plt.legend(['sen(x)'])
plt.legend(['n = 3'])
plt.legend(['n = 5'])
plt.legend(['n = 7'])
plt.legend(['n = 9'])
plt.show()