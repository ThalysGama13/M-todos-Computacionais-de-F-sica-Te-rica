from math import factorial
n = int(input('Digite um num '))

triângulo = list()
for c in range(0,n):
    for j in range(0,n+c-1):
        comb=factorial(c)/(factorial(j)*factorial(j-c))
        triângulo.append(comb)
    print(comb)