import numpy as np

lista = np.loadtxt("gravidade.dat")

cont = soma = desvio_padrao = 0
for i in lista:
    cont += 1 
    soma += i
media = soma/cont
for i in lista:
    desvio_padrao += ((1/(cont -1))*(i-media)**2)**(1/2)

print(f'O valor da Gravidade é {media:.2f} +/- {desvio_padrao:.2f}')
