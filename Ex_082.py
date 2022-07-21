valores = []
while True:
    num = int(input('Digite um valor: '))
    if num not in valores:
        valores.append(num)
    else:
        valores.append(int(input('Valor repetido. Digite um número válido: ')))
    opcao = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if opcao == 'N':
        break
print(f'No final, nossa lista contém os seguintes valores: {(sorted(valores))}')

