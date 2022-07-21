tabela = ('Palmeiras', 'Atlético-PR', 'Atlético-MG', 'Corinthians', 'Internacional', 'Fluminense', 'São Paulo',
          'Flamengo', 'Santos', 'Botafogo', 'Avaí', 'Coritiba', 'América-MG', 'Bragantino', 'Ceará', 'Atlético-GO',
          'Goiás', 'Cuiabá', 'Juventude', 'Fortaleza')
saopaulo = tabela.index('São Paulo')
print(f'Os cinco primeiros colocados do Brasileirão: {tabela[0:5]}')
print('-*' * 25)
print(f'Os quatro últimos colocados do Brasileirão: {tabela[16:20]}')
print('-*' * 25)
print(f'Os times organizados em ordem alfabética: {sorted(tabela)}')
print('-*' * 25)
print(f'O time do São Paulo está na {saopaulo} posição.')



