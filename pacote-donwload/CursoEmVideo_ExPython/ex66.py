cont = soma = 0
while True:
    num = int(input('Digite um número '))
    if num == 999:
        break
    cont += 1
    soma += num

print(f'Você DIGITOU {cont} números e a soma total foi de {soma} ')