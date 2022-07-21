distancia = float(input('Bem-vindo a nossa rodoviária! Digite a distância da sua viagem em KM: '))
if distancia <= 200:
    preco1 = distancia * 0.50
    print(f'O preço da passagem será R$ {preco1 :.2F}. ')
else:
    preco2 = distancia * 0.45
    print(f'O preço da passagem será R$ {preco2 :.2F}. ')



