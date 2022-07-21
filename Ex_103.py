from random import randint

numsort = list()

def sorteia():
    numsort.clear()
    for c in range(0, 5):
        numsort.append(randint(0, 10))
    print(numsort)

def soma():
    soma = 0
    for i in numsort:
        if i % 2 == 0:
            soma = i + soma
    print(f'A soma dos valores pares em {numsort} é de {soma}')


sorteia()
soma()





