from datetime import date
ano = date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    pessoas = int(input(f'Me dê o ano do nascimento da {c}ª pessoa: '))
    idade = ano - pessoas
    if idade >= 18:
        maior += 1
    else:
        menor += 1

print(f'No grupo temos {maior} maiores de idade.')
print(f'No grupo, temos {menor} menores de idade.')
