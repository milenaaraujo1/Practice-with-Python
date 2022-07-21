from datetime import date
ano = date.today().year

pessoa = dict()
pessoa['nome'] = str(input('Nome: '))
pessoa['idade'] = int(input('Ano de nascimento: '))
pessoa['ctps'] = int(input('Carteira de Trabalho [0 não tem]: '))

if pessoa['ctps'] != 0:
    pessoa['contratação'] = int(input('Ano de contratação: '))
    pessoa['salário'] = float(input('Salário: '))

    idade = pessoa['contratação'] - pessoa['idade']
    pessoa['aposentadoria'] = idade + 35

pessoa['idade'] = ano - pessoa['idade']

print('-=' * 30)
for k, v in pessoa.items():
    print(f'- {k} tem valor {v}.')

