ano = int(input('DIGITE O ANO PARA VERIFICAR SE ELE É BISSEXTO '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('ANO BISSEXTO')
else:
    print('NÃO É BISSEXTO')