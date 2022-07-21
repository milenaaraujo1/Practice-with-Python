print('Gerador de Progressão aritmética')
print('*-' * 10)
termo1 = int(input('Digite o primeiro termo: ' ))
primeiro = termo1
razao = int(input('Agora, digite a razão: '))
cont = 1
limite = 10
while cont <= limite:
    print(f'{termo1}', end=' > ')
    termo1 += razao
    cont += 1
    if cont > limite:
        cont = 1
        limite = int(input('Deseja mostrar mais quantos termos? '))
if limite == 0:
    print('Fim')




