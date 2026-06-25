salario = float(input('Qual valor do seu salario R$  '))
if salario <= 1250:
    aumento = salario + (salario * 15 / 100)
    print(f'Seu salario atual era de R${salario} com aumento de 15% passou a ser de {aumento}')
else:
    aumento = salario + (salario * 10 / 100)
    print(f'Seu salario atual era de R${salario} com aumento de 10% passou a ser de {aumento}')