import random
print('Bem-vindo ao nosso sorteador')
a1 = input('Digite o nome do primeiro aluno: ')
a2 = input('Agora, do segundo aluno: ')
a3 = input('Agora, o terceiro aluno: ')
a4 = input('Por fim, o quarto aluno: ')
lista = [a1, a2, a3, a4]
sort = random.choice(lista)
print(f'O aluno(a) sorteado foi {sort}')

