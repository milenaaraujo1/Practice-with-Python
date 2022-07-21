palavras = ('Milena', 'Victor', 'Marina', 'Mariana', 'Thiago', 'Alice')
vogais = ('a', 'e', 'i', 'o', 'u')
for p in palavras:
    print(f'\nNa palavra {p} temos: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')


