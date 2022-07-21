print('*-' * 10)
print('Gerador de Sequência Fibonacci')
print('*-' * 10)
sequencia = int(input('Quantos termos deseja mostrar? '))
cont = 1
anterior = 0
proxima = 1
soma = 1
while cont <= sequencia:
    print(anterior, end='-')
    cont += 1
    soma = proxima + anterior
    anterior = proxima
    proxima = soma
print('Fim')

