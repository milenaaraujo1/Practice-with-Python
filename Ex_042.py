from datetime import date
nome = str(input('Olá! Qual o seu nome? ')).strip()
anonascimento = int(input('Digite o ano do seu nascimento: ' ))
anoalistamento = anonascimento + 18
ano = date.today().year
mes = date.today().month
dia = date.today().day
if anonascimento + 18 == ano:
    print(f'{nome}, você precisa se alistar entre os primeiros seis meses deste ano. E já estamos no dia {dia} do mês {mes}! ')
elif mes > 6 and anoalistamento == ano:
    print(f'{nome}, você perdeu o prazo do alistamento. Favor se reportar a um posto do Exército do Brasil')
elif anoalistamento < ano:
    print(f'{nome}, você deveria ter se alistado entre janeiro e junho de {anoalistamento}!')
else:
    anoalistamento > ano
    print(f'{nome}, você deverá se alistar entre janeiro e junho do ano de {anoalistamento}!')
