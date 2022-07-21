'''ano = int(input('Digite um ano qualquer e vamos descobrir se ele é bissexto: '))
if (ano%4) == 0 and (ano%100) != 0:
   if ano > 2022: print(f'O ano {ano} será bissexto!')
   else: print(f'O ano {ano} foi bissexto! ')

else:
    if ano > 2022: print(f'O ano {ano} não será bissexto!')
    else: print(f'O ano {ano} não foi bissexto!')'''
from datetime import date
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 00:
    print(f'O ano {ano} é bissexto')
else:
    print(f'O ano {ano} não é bissexto')


