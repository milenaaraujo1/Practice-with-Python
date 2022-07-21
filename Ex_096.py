jogador = dict()
gols = list()
total = 0
jogador['nome'] = str(input('Digite o nome do jogador: '))
jogador['partidas'] = int(input('Quantas partidas ele jogou? '))

for c in range(0, jogador['partidas']):
    gols.append(int(input(f'Quantos gols ele fez na partida {c}? ')))
    jogador['gols'] = gols
    jogador['total'] = sum(gols)

print('-=' * 30)
print(jogador)
print('-=' * 30)

for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}.')

print('-=' * 30)

print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas: ')
for c in range(0, jogador['partidas']):
    print(f' -> Na partida {c}, fez {gols[c]} gols.')


