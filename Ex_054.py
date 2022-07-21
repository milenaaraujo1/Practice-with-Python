termo1 = int(input('Digite o  primeiro termo da sua progressão: '))
razao = int(input('Agora, digite a razão dessa progressão: '))
decimo = termo1 + (10 - 1) * razao
for c in range(termo1, decimo + razao, razao):
    print(f'{c}', end=' > ')
print('ACABOU')


