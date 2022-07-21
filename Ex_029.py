frase = str(input('Digite uma frase: ')).strip()
frase1 = (frase.upper()) ##transformei em maiuscula se não o programa não reconhece
frase2 = (frase1.count('A')) ## contar quantas vezes a letra 'a' aparece
frase3 = (frase1.find('A') + 1) ##descobrindo em que posição ela aparece pela primeira vez
frase4 = (frase1.rfind('A') + 1) #descobrindo onde a aparece pela ultima vez
print(f'A letra a aparece {frase2} vezes ')
print(f'A letra a aparece pela primeira vez na posição {frase3}')
print(f'A letra a aparece pela ultima vez na posição {frase4}')




