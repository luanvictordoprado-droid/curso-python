a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
if a + b > c and a + c > b and b + c > a:
    print(f'Você DIGITOU os valores {a},{b} e {c} eles formam um triângulo')
else:
    print(f'Você DIGITOU os valores {a},{b} e {c} eles não formam um triângulo')