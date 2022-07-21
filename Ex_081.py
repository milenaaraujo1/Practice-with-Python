valores = []
for c in range(0, 5):
    valores.append(int(input(f'Digite o {c+1}ª valor: ')))
print(f'Nossa lista de números é: {valores}')
print(f'O maior valor digitado foi o {max(valores)} na posição {valores.index(max(valores))+1}')
print(f'O menor valor digitado foi o {min(valores)} na posição {valores.index(min(valores))+1}')


