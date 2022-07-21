lista = []
impares = []
pares = []
while True:
    n = int(input('Digite um valor: '))
    opcao = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]

    if (n % 2) == 0:
        pares.append(n)
    else:
        impares.append(n)

    lista = pares + impares
    if opcao == 'N':
        break

print(f'A lista completa é {lista}.')
print(f'Os números ímpares digitados são: {impares}')
print(f'Os númreros pares digitados são: {pares}')

