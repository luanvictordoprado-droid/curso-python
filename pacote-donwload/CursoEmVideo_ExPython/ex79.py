numeros = list()

while True:
    n = int(input('Digite um valor: '))

    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado, não vou adicionar!')

    r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r == 'N':
        break

print(f'Sua lista é {numeros}')
print(f'Sua lista em ordem crescente: {sorted(numeros)}')  # ✅