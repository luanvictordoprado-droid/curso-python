num1 = int(input('Digite um valor: '))
num2 = int(input('Digite outro valor: '))
num3 = int(input('Digite outro valor: '))
num4 = int(input('Digite outro valor: '))

tupla = (num1, num2, num3, num4)

print(f'Voce digitou os valores {tupla}')

if 9 in tupla:
    print(f'O valor 9 apareceu {tupla.count(9)} vezes')
else:
    print('O numero 9 não apareceu')

if 3 in tupla:
    print(f'O numero 3 apareceu {tupla.index(3)} posição')

else:
    print(f'O numero 3 não apareceu')
for n in tupla:
    if n % 2 == 0:
        print(f'Os números pares foram {n}')
