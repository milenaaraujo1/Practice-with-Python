n = 0
c = 0
soma = 0
n = int(input('Digite um número [999 para parar]: '))
while n != 999:
    c += 1
    soma += n
    n = int(input('Digite um número [999 para parar]: '))
print(f'Foram mostrados {c} números. A soma entre eles é: {soma}')
