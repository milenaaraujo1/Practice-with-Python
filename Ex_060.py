g = str(input('Digite o seu gênero [F/M/N]: ')).strip().upper()[0]
while g != 'F' and g != 'M' and g != 'N':
    g = str(input('Por favor, digite um código válido [F/M/N]: ')).strip().upper()[0]
print(f'Obrigada! Genero {g} registrado com sucesso! ')

