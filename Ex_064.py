termo1 = int(input('Digite o  primeiro termo da sua progressão: '))
razao = int(input('Agora, digite a razão dessa progressão: '))
decimo = termo1 + (10 - 1) * razao
while termo1 <= decimo:
    print(termo1 , end=' > ')
    termo1 = termo1 + razao
print('FIM', end='')
