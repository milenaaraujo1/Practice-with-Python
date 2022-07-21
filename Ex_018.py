dia = int(input('O carro ficou alugado por quantos dias? '))
km = float(input('O carro percorreu quantos km? '))
pag = (dia * 60) + (km * 0.15)
print(f'O valor total do aluguel do carro pelo período e a quantidade de km rodados é de {pag :.2F}R$')

