s = 0
cont = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        cont = cont + 1
        s = s + n
print(f'A soma dos {cont} valores é {s}')



