lista = list ()
cont = 0

while True:
    n = int(input('Digite um numero: '))
    lista.append(n)
    cont += 1
    perg = str(input('Quer continuar [S/N]  ')).upper().strip()[0]
    if perg == 'N':
        break

if  5 in lista:
        print('O valor 5 está na lista')

else:
        print('O valor 5 não se encontra na lista')

print(f'A lista digitada foi {lista}')
print(f'Foram digitados {cont} numeros ')
print(f'A lista em ordem decrescente é {sorted(lista, reverse=True)}')