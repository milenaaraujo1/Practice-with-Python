matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = maior = coluna = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]
        coluna += matriz[l][2]

print('=-' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

print(f'A soma dos valores pares: {par}')
print(f'A soma dos valores da terceira coluna:{coluna}')
print(f'O maior número da segunda linha é: {max(matriz[1])}')

