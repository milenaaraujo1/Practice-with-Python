print('=-*' * 15)
print('GERADOR DE TABUADAS')
print('=-*' * 15)
c = 0
while True:
    n = int(input('Deseja ver a tabuada de qual número? '))
    print('=-*' * 15)
    if n > 0:
        for c in range(1, 11):
            print(f'{n} X {c} = {n * c}')
    else:
        break
print('=-*' * 15)
print('PROGRAMA TABUADA ENCERRADO. VOLTE SEMPRE!')


