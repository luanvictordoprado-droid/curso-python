real = float(input('Digite quanto vc possui na carteira: R$ '))
dolar = real / 5.01
euro = real / 6.00
print(f'Com R$ {real:.2f} voce consegue comprar US$ {dolar:.2f} e € {euro:.2f}.')