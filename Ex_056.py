'''p1 = input('Escreva uma expressão: ').upper().replace(' ', '')
palindromo = p1[::-1]
if p1 == palindromo:
    print(f'A expressão digitada é um Palíndromo.')
else:
    print(f'A expressão digitada não é um Palíndromo.')'''

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso +=junto[letra]
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')