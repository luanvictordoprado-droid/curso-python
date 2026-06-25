'''teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)'''

galera = list()
dado = list()
totalmai = 0
totalmen = 0
for cont in range(5):
    dado.append(str(input('Nome ')))
    dado.append(int(input('Idade ')))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade ')
        totalmai += 1
    else:
        print(f'{p[0]} não é maior de idade')
        totalmen += 1

print(galera)
print(f'O total de maiores de idade é {totalmai}')
print(f'O total de menores de idade é {totalmen}')