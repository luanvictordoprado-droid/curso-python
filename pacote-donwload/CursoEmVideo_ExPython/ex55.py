maior = 0
menor = 0
for p in range(5):
    peso = float(input(f"Digite o {p+1} peso: KG "))
    if p == 0:
        maior = menor = peso

    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso


print(f'O maior peso lido foi {maior}Kg')
print(f'O menor peso lido foi {menor}Kg')

