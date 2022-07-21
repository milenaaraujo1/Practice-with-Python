n = int(input('Digite um número para calcular o seu Fatorial: '))
c = n
f = 1
print(f'Calcuando {n}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f = f * c
    c -= 1
print(f'{f}')
