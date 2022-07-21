'''import math
print('Bem-vindo!')
angulo = float(input('Digite o ângulo desejado: '))
ra = math.radians(angulo)
co = math.cos(angulo)
se = math.sin(angulo)
tan = math.tan(angulo)
print(f'O cosseno de {angulo} graus é {co :.2F}, o seno é {se :.2F} e a tangente é {tan :.2F}')'''

import math
an = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(an))
print(f'O ângulo {an} tem o SENO {seno :.2F}')
cosseno = math.cos(math.radians((an)))
print(f'O ângulov {an} tem o COSSENO de {cosseno :.2F}')
tangente = math.tan(math.radians(an))
print(f'O ângulo {an}^tem a TANGENTE {tangente :.2F}')

