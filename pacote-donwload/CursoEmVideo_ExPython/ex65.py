soma = 0
cont = 0
media = 0
continuar = 'S'

num = int(input('Digite um número inteiro: '))
maior = num
menor = num

while continuar != 'N':
    soma += num
    cont += 1
    media = soma / cont

    if num > maior:
        maior = num
    if num < menor:
        menor = num

    continuar = input('Quer continuar? [S/N] ').upper().strip()

    if continuar != 'N':
        num = int(input('Digite um número inteiro: '))

print(f'O maior número digitado foi {maior} e o menor {menor}')
print(f'A média foi de {media:.1f}')
print(f'Você DIGITOU {cont} números')
