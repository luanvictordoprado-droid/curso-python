numeros = list()
for c in range(0, 5):
    numeros.append(int(input(f'Digite um numero para a posição {c} : ')))
print(f'Sua lista é {numeros}')
for c , n in enumerate(numeros):
    print(f'Achei na posição {c} o valor {n}')


print(f'O maior numero é {max(numeros)} na posição {numeros.index(max(numeros))}')
print(f'O menor numero é {min(numeros)} na posição {numeros.index(min(numeros))}')
