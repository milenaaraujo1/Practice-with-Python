'''n1 = int(input('Digite um número: '))
contador = 0
for c in range(1, n1 + 1):
    if (n1 % c) == 0:
        contador += 1
print(f'O número {n1} foi divísivel {contador} vezes!')
if contador == 2:
    print(f'O número {n1} é primo.')
else:
    print(f'O número {n1} não é primo.')'''

n1 = int(input('Digite um número: '))
tot = 0
for c in range(1, n1 + 1):
    if n1 % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print(f'{c}', end='')
print(f'\n\033[mO número {n1} foi divisível {tot} vezes.')
if tot == 2:
    print('Por isso ele é PRIMO!')
else:
    print('Por isso ele NÃO É PRIMO!')



