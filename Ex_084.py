c = 0
lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    opcao = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    c += 1
    if opcao == 'N':
        break

print('*-*' * 15)
if 5 not in lista:
    print(f'\nO número 5 não está na nossa lista.')
else:
    print(f'O numero 5 está na nossa lista')

lista1 = sorted(lista, reverse=True) # lista em ordem decrescente

print(f'Foram digitados {c} números.')
print(f'Os números em ordem decrescente: {lista1}.')


