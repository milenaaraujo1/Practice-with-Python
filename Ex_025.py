nome = str(input('Qual seu nome? ')).strip()
nome1 = nome.replace(" ","")
tamanho1 = (len(nome1))
nome2 = (nome.split())
tamanho2 = (len(nome2[0]))
print('Seu nome em letras maiusculas: ' + (nome.upper()))
print('Seu nome em letras minusculas: ' + (nome.lower()))
print(f'Seu nome completo tem um total de {tamanho1} letras!')
print(f'Seu primeiro nome tem {tamanho2} letras!')





