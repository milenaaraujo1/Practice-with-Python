from random import randint
from time import sleep
print('=-' * 5, end='')
print('SORTEIO MEGA-SENA', end='')
print('=-' * 5)
jogos = []
interacao = int(input('Quantos jogos você deseja sortear? '))
for l in range(0, interacao):
    while len(jogos) < 6:
        n = randint(1, 60)
        if n not in jogos:
            jogos.append(n)
    sleep(0.2)
    print(f'Sorteando o {l+1}ª jogo: {jogos[0:6]}')
    jogos.clear()
print('BOA SORTE!')





