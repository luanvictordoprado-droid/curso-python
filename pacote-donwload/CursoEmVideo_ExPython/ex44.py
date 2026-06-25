preco = float(input('Digite o valor  do produto  '))
print('''FORMAS DE PAGAMENTO
[1]AVISTA
[2]CARTÃO A VISTA
[3]CARTÃO EM 2X 
[4] CARTÃO EM 3X OU MAIS ''')
forma_pagamento = input('Digite a forma de pagamento ')
if forma_pagamento == '1':
    desconto = preco - (preco * 0.10)
    print(f'SUA FORMA DE PAGAMENTO FOI A VISTA E COM ISSO VC OBTEVE 10% DESCONTO PREÇO INICIAL R${preco} , preço final R${desconto}')
elif forma_pagamento == '2':
    desconto = preco - (preco * 0.05)
    print(f'SUA FORMA DE PAGAMENTO FOI A VISTA no CARTÃ E COM ISSO VC OBTEVE 5% DESCONTO PREÇO INICIAL R${preco} , preço final R${desconto}')
elif forma_pagamento == '3':
    print(f'FORMA DE PAGAMENTO CARTÃO EM 2X VALOR SEM ALTERARÇÃO R${preco}')

elif forma_pagamento == '4':
    desconto = preco + (preco * 0.20)
    print(f'SUA FORMA DE PAGAMENTO FOI  CARTÃo em 3x E COM ISSO VC OBTEVE 20% DE JUROS  PREÇO INICIAL R${preco} , preço final R${desconto}')
else:
    print('OPÇÃO INVALIDA')