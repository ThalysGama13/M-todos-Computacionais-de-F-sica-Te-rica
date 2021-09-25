'''
Essa tarefa tem vários itens'''

'item a) volume do cilíndro'

def volCilindro(h,r):
    from math import pi
    v = pi * h* r**2
    return v


'item b) média ponderada. atribue os valores e os respectivos pesos'
def mediapond(n1,n2,p1=1,p2=1):
    mp = (n1*p1 + n2*p2)/(n1 + n2)
    return mp


'item c) somente pares. uma função que recebe uma lista de números inteiros e retorna somente os valore pares'
def somente_pares(lista):
    pares = []
    for n in lista:
        if n % 2 == 0:
            pares.append(n)
    return pares


'''
item d) Duas funções. 
A primeira retorna a inclinação da que passa pelos pontos (x1,y1) e (x2,y2)
e a segunda que mostra o coeficiente linear da equação'''
def inclinação(x1,y1,x2,y2):
    a = (y2 - y1)/(x2 - x1)
    return a


def intersecta(x1,y1,x2,y2):
    b = y2 - inclinação(x1,y1,x2,y2)*0
    return b


#def stats(valores: np.array):


'''
f) escalar. função que faz o produto escalar'''
def escalar(x,y):
    import numpy as np
    x1 = float
    x2 = float
    y1 = float
    y2 = float
    x = np.array([[x1],[x2]])
    y = np.array([[y1],[y2]])
    e = [[x[0]*y[0]],[x[1]*y[1]]]
    return e

'''
h) Função que diz se o número é primo ou não'''
#def primo(x):
    


'''
i) Função que retorna o ln de um número'''
def l(x,n):
    x = float(x)
    n = int(n)
    soma = 0
    for c in range(0,n):
        soma += (1/c)*(x/(1+x))
    return soma


'''
j) função que calcula as raízes da equação do segundo grau a partir
dos coeficientes'''
def root(a,b,c):
    from numpy.lib.scimath import sqrt
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-b + delta**(1/2))/(2*a)
        x2 = (-b - delta**(1/2))/(2*a)
        return x1, x2
    if delta < 0:
        x1 = (-b + sqrt(delta))/(2*a)
        x2 = (-b - sqrt(delta))/(2*a)
        return x1, x2
    if delta == 0:
        x1 = x2 = -b/(2*a)
        return f' são duas raízes iguais a {x1}'


'''
k) Função que soma os elementos de uma lista'''
def mysum(lista):
    lista = []
    soma = 0
    for i in lista:
        soma += i
    return soma


'''
l) Função que converte uma quantidade de segundos para um número inteiro
de horas, minutos e segundos'''


'''
m) Função que faz o contratio da função do item l)'''
def parasegundos(horas, min, segs):
    x = float(x)
    horas = x/3600
    min = (x%3600)/60
    segs = x - horas - min
    return f' Os {x} segundos dados representam: {horas} horas, {min} minutos e {segs} segundos'
