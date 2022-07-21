n1 = int(input('Digite o primeiro número inteiro: '))
n2 = int(input('Agora, o segundo: '))
n3 = int(input('E o terceiro: '))
numbers = [n1, n2, n3]
min_value = min(numbers)
max_value = max(numbers)
print('O maior número é: ', max_value)
print(f'O menor número é: ', min_value)