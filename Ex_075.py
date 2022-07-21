contagem = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesste', 'dezoito', 'dezenove', 'vinte')
n = int(input('Digite um número de 0 a 20: '))
while True:
    if n > 20:
        n = int(input('Tente novamente. Digite um número de 0 a 20: '))
    if n < 0:
        n = int(input('Tente novamente. Digite um número de 0 a 20: '))
    else:
        break
print(f'Você digitou o número {contagem[n]}.')

