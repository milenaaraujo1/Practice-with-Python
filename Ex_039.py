print('-*' * 10)
comprador = str(input('Bem-vindo a Milena Financiamentos! Qual o seu nome? ')).strip()
print('-*' * 10)
salario = float(input('E qual o seu salário mensal? R$ '))
print('-*' * 10)
imovel = float(input(f'Certo, {comprador}. Qual o valor do imóvel que você deseja financiar? R$ '))
print('-*' * 10)
pagamento = int(input(f'Só mais uma coisa {comprador}, em quantos anos pretende quitar o imóvel? '))
print('-*' * 10)
valorparcela = (imovel/pagamento) / 12
if valorparcela > salario * (30/100):
    print(f'Infelizmente, {comprador}, seu financiamento não foi aprovado. O valor da parcela ficaria no total de {valorparcela:.2F}R$, ultrapassando 30% de sua renda!')
else:
    print(f'Parabéns {comprador}! Seu financiamento foi aprovado! As parcelas mensais ficarão no valor de {valorparcela:.2F}R$ durante {pagamento} anos!')

