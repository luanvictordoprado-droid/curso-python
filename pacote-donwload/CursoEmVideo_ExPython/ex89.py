ficha = list()
while True:
    nome = str(input('Nome :  '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar ? [S/N]')).upper().strip()[0]
    if resp == 'N':
        break

for i, a in enumerate(ficha):
    print(f'Numero {i}  Nome : {a[0]}   Media  : {a[2]}')

while True:
    opc = int(input('Mostrar notas de qual aluno ?(999 interrompe): )'))
    if opc == 999:
        break
    if opc <= len(ficha) - 1 :
        print(f'As notas do aluno {ficha[opc][0]} são {ficha[opc][1]}')

