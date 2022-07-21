numero = int(input('Digite um número entre 0 e 9999: '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')




#print('Unidade: ' + (numero[3]))
#print('Dezena: ' + (numero[2]))
#print('Centena: ' + (numero[1]))
#print('Milhar: ' + (numero[0]))
