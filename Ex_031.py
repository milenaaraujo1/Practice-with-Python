'''import random
nome = str(input('Olá. Qual o seu nome? '))
print(f'Prazer te conhecer, {nome}')
resposta = str(input(f'Vamos jogar um jogo? Digite SIM ou NÃO: ')).upper().strip()
if resposta == 'SIM':
    print(f'Ótimo {nome}! Se for assim, vou me apresentar... Me chamo CP.')
else:
    print(f'Não é como se você tivesse escolha, não é?')
print(f'Eu vou pensar em um número e você precisa adivinhar ok?')
print(f'HEY, CALMA! Não são TODOS os números né? Vamos trabalhar de 1 até 5... e não vale números quebrados')
numeroplayer = int(input('Digite sua escolha aqui: '))
numeros = [1, 2, 3, 4, 5]
numeropc = random.choice(numeros)
if numeroplayer == numeropc:
    print(f'PARABÉNS {nome.upper()}, você realmente me surpreendeu, eu pensei no número {numeropc}. Está livre para ir...')
else:
    print(f'Bom... {nome}, estou meio decepcionado... vamos ter que jogar mais um pouco, não é? Eu pensei no número {numeropc}. ')'''''

from random import randint
from time import sleep
computador = randint(0, 5) # faz o computador "PENSAR"
print('-=-' * 10)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
jogador = int(input('Em que número eu pensei? ')) # jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print(f'GANHEI! Eu pensei no número {computador} e não no número {jogador}.')