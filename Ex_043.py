print('*-' * 10)
print('Olá, este é portal de médias da Escola Milena Educação!')
print('*-' * 10)
aluno = str(input('Qual o nome completo do aluno(a)? ')).strip()
nota1 = float(input('Digite a nota da primeira bimestral: '))
nota2 = float(input('Digite a nota da segunda bimestral: '))
media = (nota1 + nota2) / 2
if media < 5.0:
    print(f'Infelizmente, {aluno} ficou com média {media :.1F} e foi reprovado(a)!')
elif media > 6.9:
    print(f'PARABÉNS! {aluno} foi aprovado(a) com média {media :.1F}!')
else:
    print(f'{aluno} ficou com média {media :.1F} e está de recuperação.')

