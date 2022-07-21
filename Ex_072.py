print('PROGRAMA DE CADASTRO')
print('-' * 15)
adultos = homens = mulheres = 0

while True:
    idade = int(input('Digite a idade: '))
    if idade >= 18:
        adultos += 1
    sexo = str(input('Agora, digite o genêro [F/M]: ')).strip().upper()[0]
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1
    opcao = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if opcao == 'N':
        break

print(f'Fim do cadastro. Ao todo, foram contabilizados {adultos} maiores de 18 anos'
      f', {homens} homens e {mulheres} mulheres com menos de vinte anos.')
