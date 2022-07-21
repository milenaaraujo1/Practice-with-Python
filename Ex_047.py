print('LOJAS MILENA!')
valor = float(input('Preço das compras R$: '))
print(''' FORMAS DE PAGAMENTO:
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão 
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    total = valor - (valor * 10 / 100)
elif opcao == 2:
    total = valor - (valor * 5 / 100)
elif opcao == 3:
    total = valor
    parcela = total / 2
    print(f'Sua compra será parcelada em 2x de {parcela} R$.')
elif opcao == 4:
    total = valor +(valor * 20/100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print(f'Sua compra será parcelada em {totparc}x de R${parcela :.2F} COM JUROS.')
else:
    total = 0
    print('OPÇÃO INVÁLIDA. TENTE NOVAMENTE.')
print(f'Sua compra de {valor :.2F} vai custar {total :.2F} R$ no final.')


'''if pagamento == 'cartão':
    parcelas = int(input('Digite aqui a quantidade de parcelas. Se for a vista, digite 0: '))
    if parcelas == 2:
        print(f'Em {parcelas :.2F} parcelas, valor do produto será {valor} R$.')
    elif parcelas >= 3:
        aumento = ((20/100) + 1)
        print(f'Com o parcelamento em {parcelas} parcelas, o valor do produto será {valor * aumento} R$')
    elif parcelas == 0:
        desconto = (valor * 5) / 100
        print(f'Com pagamento a vista no {pagamento}, o valor do produto será de {valor - desconto} R$')
else:
    pagamento == 'dinheiro' or 'cheque'
    desconto = (valor * 10) / 100
    print(f'Com pagamento em {pagamento}, o valor do produto será de {valor - desconto :.2F} R$')'''''
