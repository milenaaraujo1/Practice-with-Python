print('LISTAGEM DE PREÇOS')
produtos = ('Lápis', 2.99, 'Borracha', 3.99, 'Caderno', 20.99,
            'Caneta', 0.99, 'Papel (folha)', 0.20)
for item in range(0, len(produtos)):
    if item % 2 == 0:
        print(f'{produtos[item]:.<30}', end=' ')
    else:
        print(f'R${produtos[item]:>7.2f}')


