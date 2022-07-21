impar = 0
par = 0
lista = [], []
for c in range(0, 7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)
lista[0].sort()
lista[1].sort()
print(f'Pares: {lista[0]}')
print(f'Ímpares: {lista[1]}')











