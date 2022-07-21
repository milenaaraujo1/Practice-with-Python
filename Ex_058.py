peso = float(input(f'Peso da 1ª pessoa KG: '))
maior = peso
menor = peso
for c in range(2, 6):
    peso = float(input(f'Peso da {c}ª pessoa KG: '))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print(f'O menor peso digitado foi {menor}KG.')
print(f'O maior peso digitado foi {maior}KG.')
