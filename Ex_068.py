conti = 0
soma = 0
c = 0
lista = []
while conti != 'N':
    n = int(input('Digite um número: '))
    soma += n
    c += 1
    conti = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    lista += [n]
media = soma / c
print(f'Foram mostrados {c} valores. A média entre eles é de {media :.1F}.')
print(f'O maior valor foi o {max(lista)} e o menor foi o {min(lista)}.')
