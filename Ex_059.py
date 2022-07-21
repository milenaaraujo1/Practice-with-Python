print(f'------ 1ª PESSOA ------')
nome = str(input(f'Nome: ')).strip()
idade = int(input(f'Idade: '))
genero = str(input(f'[F/M]: ')).upper().strip()
idadegeral = idade
if genero == 'M':
    maior = idade
    nomemaior = nome
else:
    maior = 0
    nomemaior = ''
if genero == 'F':
    feminino = 1
else:
    feminino = 0

for c in range(2, 5):
    print(f'------ {c}ª PESSOA ------')
    nome = str(input(f'Nome: ')).strip()
    idade = int(input(f'Idade: '))
    genero = str(input(f'[F/M]: ')).upper().strip()

    idadegeral = (idadegeral + idade) / 2  ## media idade

    if genero == 'M': ## homem mais velho
        if maior < idade:
            maior = idade
            nomemaior = nome

    if genero == 'F' and idade < 20: ## mulheres com menos de 20
        feminino += 1

print(f'No grupo, existem {feminino} mulheres com menos de 20 anos')
print(f'O homem mais velho é o {nomemaior}')
print(f'A média de idade do grupo é de {idadegeral :.1F} anos.')

