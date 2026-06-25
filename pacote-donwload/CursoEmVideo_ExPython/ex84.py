temp = []
princ = []
maior = 0
menor = 0

while True:
    temp.append(str(input("Digite um nome: ")))
    temp.append(float(input("Digite um peso: ")))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    p = str(input("Quer continuar ? [S/N] ").upper().strip()[0])
    princ.append(temp[:])
    temp.clear()
    if p == "N":
        break

print(f'Foram cadastradas {len(princ)} pessoas.')
print(princ)
print(f'O maior peso foi de {maior} e o menor peso foi de {menor}.')
for p in princ:
    if p[1] == maior:
        print(f'O maior peso foi de [{p[0]}]')