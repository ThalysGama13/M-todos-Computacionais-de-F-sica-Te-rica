R = 1.097*10**(-2)
'n>m onde ne m são inteiros positivos'
print('-'*20)
print('Série para m = 1')
print('-'*20)
for c in range(2,7):
    l1 = float(1/(R*(1 - 1/c**2)))
    print(f'{l1:.2f} nm')
    print(end=' ')

print('-'*20)
print('Série para m = 2')
print('-'*20)
for c in range(3,8):
    l2 = float(1/(R*(1/4 - 1/c**2)))
    print(f'{l2:.2f} nm')
    print(end=' ')

print('-'*20)
print('Série para m = 3')
print('-'*20)
for c in range(4,9):
    l3 = float(1/(R*(1/9 - 1/c**2)))
    print(f'{l3:.2f} nm')
