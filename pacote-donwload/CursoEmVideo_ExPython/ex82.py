lista = list()
par = list()
impar = list()

while True:
    n = int(input('Digite um numero: '))
    lista.append(n)

    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)

    perg = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if perg == 'N':
        break

print(f'Lista completa: {lista}')
print(f'Lista PAR: {par}')
print(f'Lista ÍMPAR: {impar}')