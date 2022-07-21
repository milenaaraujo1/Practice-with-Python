cadastro = dict()
lista = list()
soma = media = 0
while True:
    cadastro.clear()
    cadastro['nome'] = str(input('Digite o nome: '))
    cadastro['idade'] = int(input('Digite a idade: '))
    soma += cadastro['idade']
    cadastro['sexo'] = str(input('SEXO [M/F]: ')).upper().strip()[0]
    if cadastro['sexo'] not in 'MF':
        cadastro['sexo'] = str(input('ERRO! Por favor, digite apenas M ou F')).upper().strip()[0]
    lista.append(cadastro.copy())
    continuacao = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if continuacao not in 'SN':
        continuacao = str(input('ERRO! Por favor, digite apenas S ou N.')).upper().strip()[0]
    if continuacao == 'N':
        break

print(f'A) Ao todo temos {len(lista)} pessoas cadastradas.')
media = soma / len(lista)
print(f'B) A média de idade é de {media:5.2f} anos.')
print(f'C) As mulheres cadastradas foram', end=' ')
for p in lista:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}', end='')
print()
print('D) Lista das pessoas que estão acima da média: ', end=' ')
for p in lista:
    if p['idade'] >= media:
        print('  ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()

