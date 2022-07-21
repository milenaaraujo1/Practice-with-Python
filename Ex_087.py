pessoal = []
dado = []
mai = men = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso KG:')))
    if len(pessoal) == 0:
        mai = men = dado[1]
    else:
        if dado[1] > mai:
            mai = dado[1]
        if dado[1] < men:
            men = dado[1]
    pessoal.append(dado[:])
    dado.clear()
    continuar = str(input('Deseja continuar? [S/N]:')).upper().strip()[0]
    if continuar == 'N':
        break
    if continuar != 'S' and 'N':
        continuar = str(input('Digite uma opção válida. [S/N]:')).upper().strip()[0]

print(f'Ao todo você cadastrou {len(pessoal)} pessoas.')

print(f'O maior peso foi de {mai}KG. Peso de ', end=' ')
for p in pessoal:
    if p[1] == mai:
        print(f'{p[0]}', end=' ')
print(f'\nO menor peso foi de {men}KG. Peso de ', end=' ')
for p in pessoal:
    if p[1] == men:
        print(f'{p[0]}', end=' ')

