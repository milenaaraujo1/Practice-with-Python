jogadores = dict()
lista = list()
gols = list()

while True:
    jogadores.clear()
    gols.clear()
    jogadores['nome'] = str(input('Digite o nome: '))
    jogadores['partidas'] = int(input('Quantas partidas ele jogou? '))

    for c in range(0, jogadores['partidas']):
        gols.append(int(input(f'Quantos gols na partida {c+1}: ')))
        jogadores['gols'] = gols[:]
        jogadores['total'] = sum(gols)

    lista.append(jogadores.copy())

    continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if continuar not in 'NS':
        continuar = str(input('ERRO! Digite S ou N. [S/N]: ')).upper().strip()[0]
    if continuar == 'N':
        break
print('=-' * 30)
print('cod ', end='')
for i in jogadores.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 50)
for k, v in enumerate(lista):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('=-' * 30)
while True:
    opcao = int(input('Deseja ver o levantamento de qual jogador? [999 para parar]: '))
    if opcao == 999:
        break
    if opcao >= len(lista):
        opcao = int(input('CÓDIGO INVÁLIDO. Tente novamente [999 para parar]: '))
    else:
        print('=-' * 30)
    print(f'>> LEVANTAMENTO JOGADOR: {lista[opcao]["nome"]}')
    for c, v in enumerate(lista[opcao]['gols']):
        print(f'   Partida {c+1}: {v} gols.')
    print('-' * 40)

print('>> VOLTE SEMPRE <<')
