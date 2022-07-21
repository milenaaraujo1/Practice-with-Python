print('Bem-vindo ao Sistema Nacional de Natação!')
idade = int(input('Digite aqui a idade do atleta: '))
if idade <= 9:
    print('Está classificado para a categoria mirim.')
elif idade <= 14:
    print('Está classificado para a categoria infantil.')
elif idade <= 19:
    print('Está classificado para a categoria júnior')
else:
    print('Está classificado para a categoria master.')
