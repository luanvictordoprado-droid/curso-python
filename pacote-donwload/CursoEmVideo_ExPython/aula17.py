'''valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
for c,valor in enumerate(valores):
    print(f'Na posição {c} encontrei o valor ... {valor}')
print('Cheguei ao final !')'''

a = [2,3,4,7]
b = a[:]
b [2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')

