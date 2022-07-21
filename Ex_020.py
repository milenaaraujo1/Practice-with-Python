'''import math
print('Bem-vindo! Vamos cácular o tamanho da hipotenusa do seu triângulo retângulo!')
co = float(input('Qual o comprimento do cateto oposto em centímetros? '))
ca = float(input('Qual o comprimento do cateto adjacente em centímetros? '))
soma = math.pow(co, 2) + math.pow(ca, 2)
hi = math.sqrt(soma)
print(f'A hipotenusa do seu triângulo retângulo é {hi :.2F}')'''

import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = math.hypot(co, ca)
print(f'A hipotenusa vai medir {hi :.2F}')


