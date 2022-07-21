from random import randint
from time import sleep
c = 0
print('JOGANDO OS DADOS...')
sleep(0.5)

jogadores = {'jogador1': randint(1, 6),
             'jogador2': randint(1, 6),
             'jogador3': randint(1, 6),
             'jogador4': randint(1, 6)}

for k, v in jogadores.items():
    sleep(0.5)
    print(f'{k} tirou {v} no dado')

print('=-' * 15)

for i in sorted(jogadores, key=jogadores.get, reverse=True):
    c += 1
    sleep(0.5)
    print(f'{c} lugar: {i} com {jogadores[i]}')

