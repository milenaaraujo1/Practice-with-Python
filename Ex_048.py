'''import random
print('Olá! Sou T200 e vou jogar JOKENPÔ com você.', end=' ')
print(JOGADAS DISPONÍVEIS:
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA )
jogador = int(input('Qual sua jogada? '))
jogadas = [1, 2, 3]
t200 = random.choice(jogadas)
## SE O JOGADOR ESCOLHER PEDRA 1
if jogador == 1 and t200 == 3: ## pedra ganha de tesoura.
    print('Você ganhou! Droga, eu escolhi tesoura... preciso calibrar...')
elif jogador == 1 and t200 == 2: ## pedra perde para o papel. T200
    print('EU GANHEI. HAHAHA, sou muito superior! Escolhi papel!')
## SE O JOGADOR ESCOLHER PAPEL 2
elif jogador == 2 and t200 == 3: ## papel perde para tesoura.
    print('EU GANHEI NOVAMENTE HAHAHA. Tesoura corta papel, né?')
elif jogador == 2 and t200 == 1: ## papel ganha de pedra.
    print('Perdi... meus sistemas estão falhando... porque eu escolhi pedra?')
## SE O JOGADOR ESCOLHER TESOURA 3
elif jogador == 3 and t200 == 2:  ## tesoura ganha de papel.
    print('Você ganhou! REVANCHE. Eu escolhi papel.')
elif jogador == 3 and t200 == 1:  ## tesoura perde de pedra.
    print('E A INTELIGÊNCIA ARTIFICIAL GANHOU NOVAMENTE. Eu escolhi pedra!')
## EMPATE
elif jogador == 3 and t200 == 3:
    print('EMPATEEE, escolher tesoura não foi uma boa escolha!')
elif jogador == 2 and t200 == 2:
    print('Empatamos... papel não é uma escolha muito forte!')
elif jogador == 1 and t200 == 1:
    print('Empatos... realmente... temos cabeça de pedra!')'''

from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções: 
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!!')
print('-=' * 11)
print(f'O Computador escolheu {itens[computador]}')
print(f'O Jogador escolheu {itens[jogador]}')
print('-=' * 11)
if computador == 0: ## computador jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')

elif computador == 1: ## computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')

elif computador == 2: ## computador jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')
