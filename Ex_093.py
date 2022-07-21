aluno = dict()
aluno['nome'] = str(input('Digite o nome do aluno: '))
aluno['média'] = float(input(f'Digite a média de {aluno["nome"]}: '))
aluno['situação'] = '0'
if aluno['média'] >= 6:
    aluno['situação'] = 'APROVADO'
else:
    aluno['situação'] = "REPROVADO"
print('-=' * 30)
for k, v in aluno.items():
        print(f' - {k} é igual a {v}')

