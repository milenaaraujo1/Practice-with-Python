salario = float(input('Digite aqui o salário R$: '))
if salario > 1250:
    aumento = (salario * 10) / 100
    print(f'O novo salário será de {aumento + salario } R$. ')
else:
    aumento = (salario * 15) / 100
    print(f'O novo salário será de {aumento + salario} R$.')