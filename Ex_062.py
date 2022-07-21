from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
print('''OPÇÕES:  
    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MOSTRAR O MAIOR
    [ 4 ] DIGITAR NOVOS NÚMEROS
    [ 5 ] SAIR ''')
opcao = 0
while opcao != 5:
    opcao = int(input('Qual a sua opção? '))
    if opcao == 1:
        n3 = n1 + n2
        print(f'A soma entre {n1} + {n2} é {n3}.')
        print('*-' * 10 )
    if opcao == 2:
        n3 = n1 * n2
        print(f'A multiplicação {n1} x {n2} é igual a {n3}.')
        print('*-' * 10)
    if opcao == 3:
        if n1 < n2:
            print(f'{n2} é o maior número.')
            print('*-' * 10)
        elif n1 > n2:
            print(f'{n1} é o maior número.')
            print('*-' * 10)
        elif n1 == n2:
            print(f'Os dois valores são iguais.')
            print('*-' * 10)
    if opcao == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    if opcao == 5:
        print('Finalizando...')
        print('*-' * 10)
        sleep(2)
        print('Programa finalizado, obrigada!')
        print('*-' * 10)


