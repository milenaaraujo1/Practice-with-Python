print('Essa é a nossa calculadora de IMC!')
peso = float(input('Digite o seu peso aqui KG: '))
altura = float(input('Agora, sua altura: '))
IMC = peso / (altura ** 2)
if IMC < 18.5:
    print(f'IMC está em {IMC :.1F}. Você está abaixo do peso ideal!')
elif IMC >= 18.5 and IMC <= 25:
    print(f'Seu IMC está em {IMC :.1F}, parabéns! Você está no peso ideal!')
elif IMC >= 25 and IMC <= 30:
    print(f'Seu IMC está em {IMC :.1F}, você está sobrepeso!')
elif IMC >= 30 and IMC <= 40:
    print(f'Seu IMC está em {IMC :.1F}, você está obeso!')
else:
    print(f'Seu IMC está em {IMC :.1F}, você está obeso mórbido!')

