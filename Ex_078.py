n = (int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')),
     int(input('Digite um número: ')))

print(f'Você digitou os números: {n}')
print(f'O número 9 apareceu {n.count(9)} vezes.')
if 3 in n:
    print(f'O valor três foi digitado pela primeira vez na posição {n.index(3)+1}.')
else:
    print('O valor três não foi digitado em nenhuma posição.')
print(f'Os valores pares digitados foram ', end='')
for c in n:
    if c % 2 == 0:
        print(c, end=' ')


