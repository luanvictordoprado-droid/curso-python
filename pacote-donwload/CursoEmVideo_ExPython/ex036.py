valor_casa= float(input('Digite o valor da casa: R$ '))
salario_comprador = float(input('Qual o valor do seu salario : R$  '))
parcelas_casa = int(input('Quantos anos deseja comprar? '))
parcela = valor_casa / (parcelas_casa * 12)
if parcela <= (salario_comprador/100)*30:
    print(f'FINANCIAMENTO APROVADO')
    print(f'O valor da sua casa é de R${valor_casa} , seu salario é de  R${salario_comprador}')
    print(f'O valor da parcela ficou de R${parcela} em {parcelas_casa} anos')
else:
    print('FINANCIAMENTO NEGADO ')
    print(f'O valor da sua casa é de R${valor_casa} , seu salario é de  R${salario_comprador}')
    print(f'O valor da parcela ficou de R${parcela} em {parcelas_casa} anos')
    print('O VALOR DA CASA COMPROMETE MAIS DE 30% DE SEU SALARIO')