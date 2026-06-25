soma = 0
terceira = 0
maior = 0
matriz  = [[0,0,0],[0,0,0],[0,0,0]]
for l in range(3):
    for c in range(3):
        matriz [l][c] = int(input(f'Digite um valor para [{l},{c}]  '))
        if matriz [l][c] % 2 == 0:
            soma += matriz [l][c]
for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
for l in range(3):
    terceira += matriz [l][2]

print(f'A soma de valores pares é de {soma}')
print(f'A soma da terceira coluna é de {terceira}')
for c in range(3):
    if c == 0:
        maior = matriz [l][c]

    elif matriz[1][c]>maior:
        maior = matriz[1][c]


print(f'O maior numero da segunda linha é {maior} ')