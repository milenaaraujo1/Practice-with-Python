print('-=' * 20)
print('Analisador de Triângulos')
print('-=' * 20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + 3 and r2 < r1 + 3 and r3 < r1 + r2:
    print('Os segmentos acima FORMAM um triângulo')
else:
    print('Os segmentos acima NÃO FORAM um triângulo')