def area(l, c):
    a = l * c
    print(f'A área de um terreno {l}x{c} metros é de {a:.1F}m² quadrados.')

# Programa principal
print('>>> Controle de terrenos <<<')

l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)
