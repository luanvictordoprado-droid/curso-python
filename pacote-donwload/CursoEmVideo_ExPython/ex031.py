bilhete = float(input('Qual a distancia em km da sua viagem  ?'))
if bilhete <= 200:
    valor = bilhete * 0.50
    print(f'Você irá percorrer {bilhete} KM  e o valor da sua passagem será de R${valor:.2f} ')
else:
    valor = bilhete * 0.45
    print(f'Você irá percorrer {bilhete} KM  e o valor da sua passagem será de R${valor:.2f} ')
print('BOA VIAGEM')