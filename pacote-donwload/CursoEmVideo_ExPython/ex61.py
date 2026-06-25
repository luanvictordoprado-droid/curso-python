primeiro = int(input("Digite o primeiro valor: "))
razao = int(input("Digite o razao: "))
termo = primeiro
cont = 1
while cont <= 10:
    print(f'=> {termo}',end='')
    termo += razao
    cont += 1