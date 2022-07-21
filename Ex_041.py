n1 = int(input('Olá! Digite um número inteiro: '))
n2 = int(input('Agora, digite um segundo número: '))
if n2 > n1:
    print(f'{n2} é maior que {n1}')
elif n1 > n2:
    print(f'{n1} é maior que {n2}')
else:
    print('Não existe valor maior, os dois são iguais!')
