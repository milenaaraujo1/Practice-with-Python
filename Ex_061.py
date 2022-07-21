import random
print('Olá! Vou pensar em um número entre 0 e 10. Tente adivinhar! ')
jogador = int(input('Qual o seu palpite? '))
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
computador = random.choice(numeros)
palpites = 1
while jogador != computador:
    palpites += 1
    if jogador > computador:
        jogador = int(input('Um pouco menos... tente novamente! '))
    if jogador < computador:
        jogador = int(input('Um pouco mais... tente novamente! '))
else:
    print(f'Acertou com {palpites} palpites! Eu também pensei no {computador}!')
