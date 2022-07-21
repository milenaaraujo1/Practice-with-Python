print('CALCULADOR DE MULTAS NA AVENIDA PEDRO II')
velocidade = float(input('Digite aqui a velocidade do carro: '))
multa = 7 * (velocidade - 80)
if velocidade >=81:
    print(f'Você foi multado! Sua multa vai custar R$ {multa:.2F}.')
else:
    print('Você estava dentro do limite permitido. Nenhuma multa será aplicada.')



