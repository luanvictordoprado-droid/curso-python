a = int(input('DIGITE UM NUMERO '))
b = int(input('DIGITE UM NUMERO '))
c = int(input('DIGITE UM NUMERO '))
if a > b and a > c:
    print(f'Numero {a} é o maior')
elif b > a and b > c:
    print(f'Numero {b} é o maior')
else:
    print(f'Numero {c} é o maior')

if a < b and a < c:
    print(f'O numero {a} é o menor')
elif b < a and b < c:
    print(f'O numero {b} é o menor ')
else:
    print(f'O numero {c} é  o menor ')